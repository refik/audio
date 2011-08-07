# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tip'
        db.create_table('bilgiGiris_tip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bilgiGiris', ['Tip'])

        # Adding model 'Sehir'
        db.create_table('bilgiGiris_sehir', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bilgiGiris', ['Sehir'])

        # Adding model 'Bilgi'
        db.create_table('bilgiGiris_bilgi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sehir', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bilgiGiris.Sehir'])),
            ('telefon', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('firma', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mesaj', self.gf('django.db.models.fields.TextField')()),
            ('tip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bilgiGiris.Tip'], null=True, blank=True)),
            ('tarih', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 8, 7, 0, 11, 41, 22578))),
        ))
        db.send_create_signal('bilgiGiris', ['Bilgi'])

        # Adding M2M table for field sorumlu on 'Bilgi'
        db.create_table('bilgiGiris_bilgi_sorumlu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bilgi', models.ForeignKey(orm['bilgiGiris.bilgi'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('bilgiGiris_bilgi_sorumlu', ['bilgi_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tip'
        db.delete_table('bilgiGiris_tip')

        # Deleting model 'Sehir'
        db.delete_table('bilgiGiris_sehir')

        # Deleting model 'Bilgi'
        db.delete_table('bilgiGiris_bilgi')

        # Removing M2M table for field sorumlu on 'Bilgi'
        db.delete_table('bilgiGiris_bilgi_sorumlu')


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
            'Meta': {'object_name': 'Bilgi'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firma': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isim': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mesaj': ('django.db.models.fields.TextField', [], {}),
            'sehir': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Sehir']"}),
            'sorumlu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'null': 'True', 'symmetrical': 'False'}),
            'tarih': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 8, 7, 0, 11, 41, 22578)'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Tip']", 'null': 'True', 'blank': 'True'})
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
