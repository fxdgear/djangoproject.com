# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Website'
        db.create_table('showcase_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('showcase', ['Website'])

        # Adding model 'DjangoFeature'
        db.create_table('showcase_djangofeature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('showcase', ['DjangoFeature'])


    def backwards(self, orm):
        
        # Deleting model 'Website'
        db.delete_table('showcase_website')

        # Deleting model 'DjangoFeature'
        db.delete_table('showcase_djangofeature')


    models = {
        'showcase.djangofeature': {
            'Meta': {'ordering': "('order',)", 'object_name': 'DjangoFeature'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'showcase.website': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Website'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['showcase']
