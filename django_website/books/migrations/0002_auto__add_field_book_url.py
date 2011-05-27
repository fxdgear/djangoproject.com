# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Book.url'
        db.add_column('books_book', 'url', self.gf('django.db.models.fields.URLField')(default='http://example.com', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Book.url'
        db.delete_column('books_book', 'url')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['books']
