from django.db import models
from django.utils.translation import gettext_lazy as _

class BookManager(models.Manager):
    
    def featured(self):
        return self.get_query_set().filter(is_featured=True)



class Book(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=100)
    sub_title = models.CharField(verbose_name=_('sub title'),
                                 max_length=100,
                                 blank=True)
    authors = models.CharField(verbose_name=_('authors'), max_length=255)
    year_published = models.IntegerField(verbose_name=_('year published'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    cover_image = models.ImageField(verbose_name=_('cover image'),
                                    upload_to='uploads/books/')
    url = models.URLField(verbose_name=_('url'))
    is_featured = models.BooleanField(
                      verbose_name=_('is featured'),
                      default=False,
                      help_text=_('If ticked this book will'
                                  'appear on the home page.')
                  )
    
    objects = BookManager()
    
    class Meta:
        ordering = ('-year_published', 'title',)
