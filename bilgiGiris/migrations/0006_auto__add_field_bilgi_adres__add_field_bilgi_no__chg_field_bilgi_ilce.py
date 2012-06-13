# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Bilgi.adres'
        db.add_column('bilgiGiris_bilgi', 'adres', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Bilgi.no'
        db.add_column('bilgiGiris_bilgi', 'no', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Changing field 'Bilgi.ilce'
        db.alter_column('bilgiGiris_bilgi', 'ilce_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bilgiGiris.Ilce'], null=True))


    def backwards(self, orm):
        
        # Deleting field 'Bilgi.adres'
        db.delete_column('bilgiGiris_bilgi', 'adres')

        # Deleting field 'Bilgi.no'
        db.delete_column('bilgiGiris_bilgi', 'no')

        # Changing field 'Bilgi.ilce'
        db.alter_column('bilgiGiris_bilgi', 'ilce_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['bilgiGiris.Ilce']))


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
            'adres': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firma': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ilce': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Ilce']", 'null': 'True', 'blank': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mesaj': ('django.db.models.fields.TextField', [], {}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sehir': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Sehir']"}),
            'sorumlu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Tip']"})
        },
        'bilgiGiris.ilce': {
            'Meta': {'object_name': 'Ilce'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sehir': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Sehir']"})
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
        }
    }

    complete_apps = ['bilgiGiris']
