# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SayfaLink.isim'
        db.add_column('ozelSayfa_sayfalink', 'isim', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SayfaLink.isim'
        db.delete_column('ozelSayfa_sayfalink', 'isim')


    models = {
        'dokuman.dokuman': {
            'Meta': {'object_name': 'Dokuman'},
            'dosya': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'resim': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'urun_sayfa': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'ortakVeri.link': {
            'Meta': {'object_name': 'Link'},
            'direklink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dokuman': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dokuman.Dokuman']", 'null': 'True', 'blank': 'True'}),
            'dosya': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Kategori']", 'null': 'True', 'blank': 'True'}),
            'sayfa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatpages.FlatPage']", 'null': 'True', 'blank': 'True'}),
            'urun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Urun']", 'null': 'True', 'blank': 'True'})
        },
        'ozelSayfa.sayfa': {
            'Meta': {'object_name': 'Sayfa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'ozelSayfa.sayfalink': {
            'Meta': {'object_name': 'SayfaLink', '_ormbases': ['ortakVeri.Link']},
            'gorunum': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'link_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ortakVeri.Link']", 'unique': 'True', 'primary_key': 'True'}),
            'sayfa_ait': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ozelSayfa.Sayfa']"}),
            'yazi': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ozelSayfa.sayfamedya': {
            'Meta': {'object_name': 'SayfaMedya'},
            'dosya': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sayfaait': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ozelSayfa.Sayfa']"}),
            'yazi': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'seri': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'sistem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['urun.Sistem']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tanitim': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['ozelSayfa']
