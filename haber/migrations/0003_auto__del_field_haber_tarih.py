# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Haber.tarih'
        db.delete_column('haber_haber', 'tarih')


    def backwards(self, orm):
        
        # Adding field 'Haber.tarih'
        db.add_column('haber_haber', 'tarih', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default='', blank=True), keep_default=False)


    models = {
        'haber.haber': {
            'Meta': {'object_name': 'Haber'},
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'icerik': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['haber']
