# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year_published', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('books', ['Book'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('books_book')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_published': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['books']
