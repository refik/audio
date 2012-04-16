# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Haber.tarih'
        db.add_column('haber_haber', 'tarih', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2012, 4, 16)), keep_default=False)

        # Changing field 'Haber.baslik'
        db.alter_column('haber_haber', 'baslik', self.gf('django.db.models.fields.CharField')(max_length=25))


    def backwards(self, orm):
        
        # Deleting field 'Haber.tarih'
        db.delete_column('haber_haber', 'tarih')

        # Changing field 'Haber.baslik'
        db.alter_column('haber_haber', 'baslik', self.gf('django.db.models.fields.CharField')(max_length=32))


    models = {
        'haber.haber': {
            'Meta': {'ordering': "['-tarih']", 'object_name': 'Haber'},
            'anasayfa': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'detay': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icerik': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['haber']
