from django.db import models
from django.utils.translation import gettext_lazy as _

class Website(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    image = models.ImageField(verbose_name=_('image'),
                              upload_to='uploads/showcase/websites/')
    url = models.URLField(verbose_name=_('url'))
    tagline = models.CharField(verbose_name=_('tagline'), max_length=255)
    order = models.IntegerField(verbose_name=_('order'))
    
    class Meta:
        ordering = ('order',)
    
    
class DjangoFeature(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    url = models.URLField(verbose_name=_('url'))
    description = models.TextField(verbose_name=_('description'))
    order = models.IntegerField(verbose_name=_('order'))
    
    class Meta:
        ordering = ('order',)
