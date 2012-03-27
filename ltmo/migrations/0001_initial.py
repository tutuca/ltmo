# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Leak'
        db.create_table('ltmo_leak', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=126, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(default='Anonymous', max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tags', self.gf('tagging.fields.TagField')(default='random')),
            ('metadata', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ltmo', ['Leak'])


    def backwards(self, orm):
        
        # Deleting model 'Leak'
        db.delete_table('ltmo_leak')


    models = {
        'ltmo.leak': {
            'Meta': {'object_name': 'Leak'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Anonymous'", 'max_length': '20'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "'random'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '126', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ltmo']
