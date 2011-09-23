# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Haber.slug'
        db.delete_column('haber_haber', 'slug')

        # Deleting field 'Haber.meta'
        db.delete_column('haber_haber', 'meta')

        # Adding field 'Haber.tarih'
        db.add_column('haber_haber', 'tarih', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.date(2011, 8, 13), blank=True), keep_default=False)

        # Changing field 'Haber.icerik'
        db.alter_column('haber_haber', 'icerik', self.gf('django.db.models.fields.CharField')(max_length=60))


    def backwards(self, orm):
        
        # Adding field 'Haber.slug'
        db.add_column('haber_haber', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, db_index=True), keep_default=False)

        # Adding field 'Haber.meta'
        db.add_column('haber_haber', 'meta', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Deleting field 'Haber.tarih'
        db.delete_column('haber_haber', 'tarih')

        # Changing field 'Haber.icerik'
        db.alter_column('haber_haber', 'icerik', self.gf('django.db.models.fields.TextField')(max_length=60))


    models = {
        'haber.haber': {
            'Meta': {'object_name': 'Haber'},
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'icerik': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['haber']
