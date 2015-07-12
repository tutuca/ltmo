# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Removing unique constraint on 'Leak', fields ['slug']
        db.delete_unique('ltmo_leak', ['slug'])

        # Changing field 'Leak.slug'
        db.alter_column('ltmo_leak', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

        # Changing field 'Leak.metadata'
        db.alter_column('ltmo_leak', 'metadata', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):

        # Changing field 'Leak.slug'
        db.alter_column('ltmo_leak', 'slug', self.gf('django.db.models.fields.SlugField')(default='random', max_length=50, unique=True))

        # Adding unique constraint on 'Leak', fields ['slug']
        db.create_unique('ltmo_leak', ['slug'])

        # Changing field 'Leak.metadata'
        db.alter_column('ltmo_leak', 'metadata', self.gf('django.db.models.fields.TextField')(default='{}'))


    models = {
        'ltmo.leak': {
            'Meta': {'object_name': 'Leak'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Anonymous'", 'max_length': '20'}),
            'changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'rendered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '126', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ltmo']
