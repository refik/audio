# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rakip'
        db.create_table('teklif_rakip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('teklif', ['Rakip'])

        # Adding model 'Sebep'
        db.create_table('teklif_sebep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('isim', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('teklif', ['Sebep'])

        # Adding field 'Teklif.kaybedilen_rakip'
        db.add_column('teklif_teklif', 'kaybedilen_rakip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teklif.Rakip'], null=True, blank=True), keep_default=False)

        # Adding M2M table for field kaybetme_sebepleri on 'Teklif'
        db.create_table('teklif_teklif_kaybetme_sebepleri', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teklif', models.ForeignKey(orm['teklif.teklif'], null=False)),
            ('sebep', models.ForeignKey(orm['teklif.sebep'], null=False))
        ))
        db.create_unique('teklif_teklif_kaybetme_sebepleri', ['teklif_id', 'sebep_id'])


    def backwards(self, orm):
        
        # Deleting model 'Rakip'
        db.delete_table('teklif_rakip')

        # Deleting model 'Sebep'
        db.delete_table('teklif_sebep')

        # Deleting field 'Teklif.kaybedilen_rakip'
        db.delete_column('teklif_teklif', 'kaybedilen_rakip_id')

        # Removing M2M table for field kaybetme_sebepleri on 'Teklif'
        db.delete_table('teklif_teklif_kaybetme_sebepleri')


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
            'sehir': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bilgiGiris.Sehir']", 'null': 'True', 'blank': 'True'}),
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
        'comments.comment': {
            'Meta': {'ordering': "('submit_date',)", 'object_name': 'Comment', 'db_table': "'django_comments'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type_set_for_comment'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_pk': ('django.db.models.fields.TextField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comment_comments'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'Meta': {'object_name': 'Teklif'},
            'bilgi': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bilgiGiris.Bilgi']", 'unique': 'True'}),
            'daire': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'durum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Durum']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kaybedilen_rakip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Rakip']", 'null': 'True', 'blank': 'True'}),
            'kaybetme_sebepleri': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['teklif.Sebep']", 'null': 'True', 'blank': 'True'}),
            'tutar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'teklif.teklifyorum': {
            'Meta': {'ordering': "('submit_date',)", 'object_name': 'TeklifYorum', '_ormbases': ['comments.Comment']},
            'comment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['comments.Comment']", 'unique': 'True', 'primary_key': 'True'}),
            'dosya': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'durum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teklif.Durum']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['teklif']
