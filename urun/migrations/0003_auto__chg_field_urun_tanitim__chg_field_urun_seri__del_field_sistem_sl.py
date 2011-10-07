# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Urun.tanitim'
        db.alter_column('urun_urun', 'tanitim', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Urun.seri'
        db.alter_column('urun_urun', 'seri', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Deleting field 'Sistem.slug'
        db.delete_column('urun_sistem', 'slug')

        # Deleting field 'Sistem.tanitim'
        db.delete_column('urun_sistem', 'tanitim')

        # Adding field 'Sistem.resim'
        db.add_column('urun_sistem', 'resim', self.gf('filebrowser.fields.FileBrowseField')(default='', max_length=150), keep_default=False)

        # Adding field 'Sistem.sema'
        db.add_column('urun_sistem', 'sema', self.gf('filebrowser.fields.FileBrowseField')(max_length=150, null=True, blank=True), keep_default=False)

        # Changing field 'Ozellik.isim'
        db.alter_column('urun_ozellik', 'isim', self.gf('django.db.models.fields.CharField')(max_length=200))


    def backwards(self, orm):
        
        # Changing field 'Urun.tanitim'
        db.alter_column('urun_urun', 'tanitim', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Urun.seri'
        db.alter_column('urun_urun', 'seri', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Adding field 'Sistem.slug'
        db.add_column('urun_sistem', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, db_index=True), keep_default=False)

        # Adding field 'Sistem.tanitim'
        db.add_column('urun_sistem', 'tanitim', self.gf('filebrowser.fields.FileBrowseField')(default='', max_length=50), keep_default=False)

        # Deleting field 'Sistem.resim'
        db.delete_column('urun_sistem', 'resim')

        # Deleting field 'Sistem.sema'
        db.delete_column('urun_sistem', 'sema')

        # Changing field 'Ozellik.isim'
        db.alter_column('urun_ozellik', 'isim', self.gf('django.db.models.fields.CharField')(max_length=50))


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
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'urun.sistem': {
            'Meta': {'object_name': 'Sistem'},
            'aciklama': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '150'}),
            'sema': ('filebrowser.fields.FileBrowseField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'tip': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'urun.urun': {
            'Meta': {'object_name': 'Urun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UrunKategori'", 'to': "orm['urun.Kategori']"}),
            'ozellik': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'UrunOzellikler'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['urun.Ozellik']"}),
            'panel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'panel_rel_+'", 'null': 'True', 'to': "orm['urun.Urun']"}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'resim_yazi': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'seri': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sistem': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['urun.Sistem']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tanitim': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'urun.yeniurun': {
            'Meta': {'object_name': 'YeniUrun'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'urun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Urun']"})
        }
    }

    complete_apps = ['urun']
