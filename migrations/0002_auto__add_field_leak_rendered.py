# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Leak.rendered'
        db.add_column('ltmo_leak', 'rendered', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Leak.rendered'
        db.delete_column('ltmo_leak', 'rendered')


    models = {
        'ltmo.leak': {
            'Meta': {'object_name': 'Leak'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Anonymous'", 'max_length': '20'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'rendered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "'random'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '126', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ltmo']
