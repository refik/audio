# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Sistem'
        db.create_table('urun_sistem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tip', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aciklama', self.gf('django.db.models.fields.TextField')()),
            ('tanitim', self.gf('filebrowser.fields.FileBrowseField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('urun', ['Sistem'])

        # Adding model 'Ozellik'
        db.create_table('urun_ozellik', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('urun', ['Ozellik'])

        # Adding model 'Kategori'
        db.create_table('urun_kategori', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('urun', ['Kategori'])

        # Adding model 'Urun'
        db.create_table('urun_urun', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('resim', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('kategori', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UrunKategori', to=orm['urun.Kategori'])),
            ('seri', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('tanitim', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('urun', ['Urun'])

        # Adding M2M table for field sistem on 'Urun'
        db.create_table('urun_urun_sistem', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('urun', models.ForeignKey(orm['urun.urun'], null=False)),
            ('sistem', models.ForeignKey(orm['urun.sistem'], null=False))
        ))
        db.create_unique('urun_urun_sistem', ['urun_id', 'sistem_id'])

        # Adding M2M table for field ozellik on 'Urun'
        db.create_table('urun_urun_ozellik', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('urun', models.ForeignKey(orm['urun.urun'], null=False)),
            ('ozellik', models.ForeignKey(orm['urun.ozellik'], null=False))
        ))
        db.create_unique('urun_urun_ozellik', ['urun_id', 'ozellik_id'])

        # Adding M2M table for field panel on 'Urun'
        db.create_table('urun_urun_panel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_urun', models.ForeignKey(orm['urun.urun'], null=False)),
            ('to_urun', models.ForeignKey(orm['urun.urun'], null=False))
        ))
        db.create_unique('urun_urun_panel', ['from_urun_id', 'to_urun_id'])

        # Adding model 'DigerModel'
        db.create_table('urun_digermodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['urun.Urun'])),
            ('resim', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('aciklama', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('urun', ['DigerModel'])

        # Adding model 'YeniUrun'
        db.create_table('urun_yeniurun', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urun', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['urun.Urun'])),
        ))
        db.send_create_signal('urun', ['YeniUrun'])


    def backwards(self, orm):
        
        # Deleting model 'Sistem'
        db.delete_table('urun_sistem')

        # Deleting model 'Ozellik'
        db.delete_table('urun_ozellik')

        # Deleting model 'Kategori'
        db.delete_table('urun_kategori')

        # Deleting model 'Urun'
        db.delete_table('urun_urun')

        # Removing M2M table for field sistem on 'Urun'
        db.delete_table('urun_urun_sistem')

        # Removing M2M table for field ozellik on 'Urun'
        db.delete_table('urun_urun_ozellik')

        # Removing M2M table for field panel on 'Urun'
        db.delete_table('urun_urun_panel')

        # Deleting model 'DigerModel'
        db.delete_table('urun_digermodel')

        # Deleting model 'YeniUrun'
        db.delete_table('urun_yeniurun')


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
