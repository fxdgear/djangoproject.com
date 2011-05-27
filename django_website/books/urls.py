from django.conf.urls.defaults import *

from .views import books

urlpatterns = patterns('',
   url(r'^$', books, name="books"),
)
