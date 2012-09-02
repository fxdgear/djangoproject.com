# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "lucid32"
  config.vm.box_url = "http://files.vagrantup.com/lucid32.box"
  config.vm.host_name = "djangocore"

  # Shared folders
  hosthome = "#{ENV['HOME']}/"
  config.vm.share_folder("v-djangoproject", "/djangoproject", ".", :nfs => true)
  config.vm.share_folder("v-hosthome", "/home/vagrant/.hosthome", hosthome)

  # Host-only network required to use NFS shared folders
  config.vm.network :hostonly, "2.3.4.5"

  # Provisioning -------------------------------------------------------------

  config.vm.provision :shell, :inline => "/djangoproject/provisioning/shell/install-chef.sh 10.12.0"
  config.vm.provision :shell, :inline => "su vagrant -c /djangoproject/provisioning/shell/init-system.sh"

  config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = "provisioning/cookbooks"
      chef.data_bags_path = "provisioning/databags"
      chef.log_level = :debug
      chef.run_list = [
          "recipe[python::pip]",
          "recipe[python::virtualenv]",
          "recipe[apache2]",
          "recipe[apache2::mod_wsgi]",
          "recipe[git]",
          "recipe[openssl]",
          "recipe[memcached]",
          "recipe[postgresql]",
          "recipe[postgresql::client]",
          "recipe[postgresql::server]",
          "recipe[djangoproject]"]
      chef.json.merge!({
          :postgresql => {
              :listen_addresses => '*'
          }})
  end
end
