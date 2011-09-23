# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Haber'
        db.create_table('haber_haber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('baslik', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('icerik', self.gf('django.db.models.fields.TextField')(max_length=60)),
            ('resim', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('haber', ['Haber'])


    def backwards(self, orm):
        
        # Deleting model 'Haber'
        db.delete_table('haber_haber')


    models = {
        'haber.haber': {
            'Meta': {'object_name': 'Haber'},
            'baslik': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'icerik': ('django.db.models.fields.TextField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['haber']
