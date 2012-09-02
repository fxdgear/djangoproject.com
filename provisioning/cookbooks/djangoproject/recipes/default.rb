# Author: Julien Phalip
# Copyright (c) Django Software Foundation and individual contributors.
# All rights reserved.


# Load local configuration ---------------------------------------------------

configuration = data_bag_item('configuration', 'configuration')


# Set up virtualenvwrapper ---------------------------------------------------

python_pip "virtualenvwrapper" do
  action :install
  not_if "test -e /usr/local/bin/virtualenvwrapper.sh"
end

bash "Configure virtualenvwrapper" do
  user "vagrant"
  code <<-EOH
  echo "export WORKON_HOME=/home/vagrant/.virtualenvs" >> /home/vagrant/.profile
  echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.profile
  echo "workon djangoproject" >> /home/vagrant/.profile
  echo "cd /djangoproject" >> /home/vagrant/.profile
  EOH
  not_if "cat /home/vagrant/.profile | grep virtualenvwrapper.sh"
end


# Create the virtual environment ---------------------------------------------

python_virtualenv "/home/vagrant/.virtualenvs/djangoproject" do
  interpreter "python2.6"
  owner "vagrant"
  action :create
  not_if "test -d /home/vagrant/.virtualenvs/djangoproject"
end

bash "Initial loading of virtualenv requirements" do
  user "vagrant"
  code <<-EOH
  source /home/vagrant/.virtualenvs/djangoproject/bin/activate
  cd /djangoproject
  pip install -r deploy-requirements.txt
  pip install -r local-requirements.txt
  EOH
  not_if "test -d /home/vagrant/.virtualenvs/djangoproject/lib/python2.6/site-packages/django"
end


# Create the database --------------------------------------------------------

bash "Create database" do
  user "vagrant"
  code <<-EOH
  # Recreate the cluster so that it uses the UTF-8 encoding
  sudo -u postgres pg_dropcluster --stop 8.4 main
  sudo -u postgres pg_createcluster --start -e UTF-8 8.4 main

  # Create the user and database
  echo "CREATE USER djangoproject WITH SUPERUSER PASSWORD 'secret';" | sudo -u postgres psql
  sudo -u postgres createdb -O djangoproject djangoproject

  # Load initial data dump
  sudo -u postgres psql -d djangoproject < /djangoproject/provisioning/initial.sql

  # Set the 'dev' version of the docs as default
  echo "UPDATE docs_documentrelease SET is_default=false" | sudo -u postgres psql -d djangoproject
  echo "UPDATE docs_documentrelease SET is_default=true WHERE version='dev'" | sudo -u postgres psql -d djangoproject
  EOH
  not_if "sudo -u postgres psql -l | grep djangoproject"
end


# Clone django and build the docs --------------------------------------------

bash "Clone Django" do
  user "vagrant"
  code <<-EOH
  sudo mkdir /django
  sudo chown vagrant /django
  cd /django
  git clone http://github.com/django/django.git .
  EOH
  not_if "test -d /django"
end

bash "Build docs" do
  user "vagrant"
  code <<-EOH
  cd /django/docs
  source /home/vagrant/.virtualenvs/djangoproject/bin/activate
  make json
  sudo mkdir -p /djangodocs/en
  sudo chown vagrant /djangodocs/en
  ln -fs /django/docs/ /djangodocs/en/dev
  EOH
  not_if "test -d /django/docs/_build/json"
end


# Create local settings and wsgi files ---------------------------------------

template "/djangoproject/local_settings.py" do
  source "local_settings.py.erb"
  variables(
      :base_settings => "django_website.settings.www",
      :developer_name => configuration['developer']['name'],
      :developer_email => configuration['developer']['email'])
  not_if "test -e /djangoproject/local_settings.py"
end

template "/djangoproject/local_settings_docs.py" do
  source "local_settings.py.erb"
  variables(
      :base_settings => "django_website.settings.docs",
      :developer_name => configuration['developer']['name'],
      :developer_email => configuration['developer']['email'])
  not_if "test -e /djangoproject/local_settings_docs.py"
end

template "/djangoproject/site-docs.wsgi" do
  source "site.wsgi.erb"
  variables(:settings_module => "local_settings_docs")
end

template "/djangoproject/site-www.wsgi" do
  source "site.wsgi.erb"
  variables(:settings_module => "local_settings")
end

template "secrets.json" do
  source "secrets.json"
  mode "0755"
end


# Configure Apache -----------------------------------------------------------

# Disable the default Apache site
execute "disable-default-site" do
  command "a2dissite default"
end

web_app "djangoproject" do
  application_name djangoproject
  template "apache.conf.erb"
  docroot "/djangoproject"
end

service "apache2" do
  action :restart
end
