# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Haber.detay'
        db.add_column('haber_haber', 'detay', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Haber.anasayfa'
        db.add_column('haber_haber', 'anasayfa', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Haber.slug'
        db.add_column('haber_haber', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Haber.detay'
        db.delete_column('haber_haber', 'detay')

        # Deleting field 'Haber.anasayfa'
        db.delete_column('haber_haber', 'anasayfa')

        # Deleting field 'Haber.slug'
        db.delete_column('haber_haber', 'slug')


    models = {
        'haber.haber': {
            'Meta': {'object_name': 'Haber'},
            'anasayfa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'detay': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icerik': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['haber']
