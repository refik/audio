# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Yapildi.rakip'
        db.add_column('teklif_yapildi', 'rakip', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['teklif.Rakip']), keep_default=False)

        # Adding field 'Yapildi.daire'
        db.add_column('teklif_yapildi', 'daire', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Yapildi.tutar'
        db.add_column('teklif_yapildi', 'tutar', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)

        # Adding field 'Yapildi.delege'
        db.add_column('teklif_yapildi', 'delege', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='delege_set', to=orm['auth.User']), keep_default=False)

        # Adding M2M table for field sebep on 'Yapildi'
        db.create_table('teklif_yapildi_sebep', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('yapildi', models.ForeignKey(orm['teklif.yapildi'], null=False)),
            ('sebep', models.ForeignKey(orm['teklif.sebep'], null=False))
        ))
        db.create_unique('teklif_yapildi_sebep', ['yapildi_id', 'sebep_id'])

        # Changing field 'Yapildi.dosya'
        db.alter_column('teklif_yapildi', 'dosya', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100))

        # Deleting field 'Teklif.rakip'
        db.delete_column('teklif_teklif', 'rakip_id')

        # Adding field 'Teklif.dosya'
        db.add_column('teklif_teklif', 'dosya', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Teklif.temsilci'
        db.add_column('teklif_teklif', 'temsilci', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True), keep_default=False)

        # Removing M2M table for field sebep on 'Teklif'
        db.delete_table('teklif_teklif_sebep')


    def backwards(self, orm):
        
        # Deleting field 'Yapildi.rakip'
        db.delete_column('teklif_yapildi', 'rakip_id')

        # Deleting field 'Yapildi.daire'
        db.delete_column('teklif_yapildi', 'daire')

        # Deleting field 'Yapildi.tutar'
        db.delete_column('teklif_yapildi', 'tutar')

        # Deleting field 'Yapildi.delege'
        db.delete_column('teklif_yapildi', 'delege_id')

        # Removing M2M table for field sebep on 'Yapildi'
        db.delete_table('teklif_yapildi_sebep')

        # Changing field 'Yapildi.dosya'
        db.alter_column('teklif_yapildi', 'dosya', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

        # Adding field 'Teklif.rakip'
        db.add_column('teklif_teklif', 'rakip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teklif.Rakip'], null=True, blank=True), keep_default=False)

        # Deleting field 'Teklif.dosya'
        db.delete_column('teklif_teklif', 'dosya')

        # Deleting field 'Teklif.temsilci'
        db.delete_column('teklif_teklif', 'temsilci_id')

        # Adding M2M table for field sebep on 'Teklif'
        db.create_table('teklif_teklif_sebep', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teklif', models.ForeignKey(orm['teklif.teklif'], null=False)),
            ('sebep', models.ForeignKey(orm['teklif.sebep'], null=False))
        ))
        db.create_unique('teklif_teklif_sebep', ['teklif_id', 'sebep_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bilgiGiris.bilgi': {
            'Meta': {'ordering': "['-tarih']", 'object_name': 'Bilgi'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firma': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mesaj': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sehir': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Sehir']"}),
            'sorumlu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Tip']"})
        },
        'bilgiGiris.sehir': {
            'Meta': {'object_name': 'Sehir'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bilgiGiris.tip': {
            'Meta': {'object_name': 'Tip'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'teklif.durum': {
            'Meta': {'object_name': 'Durum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'kapali': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'teklif.rakip': {
            'Meta': {'object_name': 'Rakip'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'teklif.sebep': {
            'Meta': {'object_name': 'Sebep'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'teklif.teklif': {
            'Meta': {'ordering': "['-bilgi__tarih']", 'object_name': 'Teklif'},
            'bilgi': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bilgiGiris.Bilgi']", 'unique': 'True'}),
            'daire': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dosya': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'durum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Durum']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temsilci': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'tutar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'teklif.yapildi': {
            'Meta': {'object_name': 'Yapildi'},
            'daire': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'delege': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'delege_set'", 'to': "orm['auth.User']"}),
            'dosya': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'durum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Durum']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kullanici': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'mesaj': ('django.db.models.fields.TextField', [], {}),
            'rakip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Rakip']"}),
            'sebep': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['teklif.Sebep']", 'symmetrical': 'False'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'teklif': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Teklif']"}),
            'tutar': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['teklif']
