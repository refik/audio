# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Urun.resim_yazi'
        db.add_column('urun_urun', 'resim_yazi', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Urun.resim_yazi'
        db.delete_column('urun_urun', 'resim_yazi')


    models = {
        'urun.digermodel': {
            'Meta': {'object_name': 'DigerModel'},
            'aciklama': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'urun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Urun']"})
        },
        'urun.kategori': {
            'Meta': {'object_name': 'Kategori'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'urun.ozellik': {
            'Meta': {'object_name': 'Ozellik'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'urun.sistem': {
            'Meta': {'object_name': 'Sistem'},
            'aciklama': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tanitim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '50'}),
            'tip': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'urun.urun': {
            'Meta': {'object_name': 'Urun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UrunKategori'", 'to': "orm['urun.Kategori']"}),
            'ozellik': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'UrunOzellikler'", 'blank': 'True', 'to': "orm['urun.Ozellik']"}),
            'panel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'panel_rel_+'", 'null': 'True', 'to': "orm['urun.Urun']"}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'resim_yazi': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'seri': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'sistem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['urun.Sistem']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tanitim': ('django.db.models.fields.TextField', [], {})
        },
        'urun.yeniurun': {
            'Meta': {'object_name': 'YeniUrun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Urun']"})
        }
    }

    complete_apps = ['urun']
