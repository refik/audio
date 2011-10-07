# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('ortakVeri_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sayfa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatpages.FlatPage'], null=True, blank=True)),
            ('dokuman', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dokuman.Dokuman'], null=True, blank=True)),
            ('kategori', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['urun.Kategori'], null=True, blank=True)),
            ('urun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['urun.Urun'], null=True, blank=True)),
            ('direklink', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('dosya', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('ortakVeri', ['Link'])

        # Adding model 'Afis'
        db.create_table('ortakVeri_afis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dosya', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('yazi', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('ortakVeri', ['Afis'])

        # Adding model 'Menu'
        db.create_table('ortakVeri_menu', (
            ('link_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ortakVeri.Link'], unique=True, primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='childeren', null=True, to=orm['ortakVeri.Menu'])),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('ortakVeri', ['Menu'])


    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('ortakVeri_link')

        # Deleting model 'Afis'
        db.delete_table('ortakVeri_afis')

        # Deleting model 'Menu'
        db.delete_table('ortakVeri_menu')


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
        'ortakVeri.afis': {
            'Meta': {'object_name': 'Afis'},
            'dosya': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'yazi': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'ortakVeri.link': {
            'Meta': {'object_name': 'Link'},
            'direklink': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dokuman': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dokuman.Dokuman']", 'null': 'True', 'blank': 'True'}),
            'dosya': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Kategori']", 'null': 'True', 'blank': 'True'}),
            'sayfa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatpages.FlatPage']", 'null': 'True', 'blank': 'True'}),
            'urun': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['urun.Urun']", 'null': 'True', 'blank': 'True'})
        },
        'ortakVeri.menu': {
            'Meta': {'object_name': 'Menu', '_ormbases': ['ortakVeri.Link']},
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'link_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['ortakVeri.Link']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'childeren'", 'null': 'True', 'to': "orm['ortakVeri.Menu']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
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
            'resim_yazi': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'seri': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'sistem': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['urun.Sistem']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tanitim': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['ortakVeri']
