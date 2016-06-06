# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'news_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'news', ['Category'])

        # Adding model 'CustomNewsPost'
        db.create_table(u'news_customnewspost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.Category'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('date_url', self.gf('django.db.models.fields.DateField')(db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image_obj', self.gf('cofeworcester.assets.fields.AssetForeignKey')(to=orm['assets.Image'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['authors.Author'], null=True, blank=True)),
            ('hide_author', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('show_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image_description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'news', ['CustomNewsPost'])

        # Adding unique constraint on 'CustomNewsPost', fields ['slug', 'date']
        db.create_unique(u'news_customnewspost', ['slug', 'date'])

        # Adding M2M table for field tags on 'CustomNewsPost'
        m2m_table_name = db.shorten_name(u'news_customnewspost_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customnewspost', models.ForeignKey(orm[u'news.customnewspost'], null=False)),
            ('tag', models.ForeignKey(orm[u'tags.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customnewspost_id', 'tag_id'])

        # Adding M2M table for field secondary_tags on 'CustomNewsPost'
        m2m_table_name = db.shorten_name(u'news_customnewspost_secondary_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customnewspost', models.ForeignKey(orm[u'news.customnewspost'], null=False)),
            ('secondarytag', models.ForeignKey(orm[u'tags.secondarytag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customnewspost_id', 'secondarytag_id'])

        # Adding M2M table for field roles on 'CustomNewsPost'
        m2m_table_name = db.shorten_name(u'news_customnewspost_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customnewspost', models.ForeignKey(orm[u'news.customnewspost'], null=False)),
            ('role', models.ForeignKey(orm[u'tags.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customnewspost_id', 'role_id'])

        # Adding M2M table for field deaneries on 'CustomNewsPost'
        m2m_table_name = db.shorten_name(u'news_customnewspost_deaneries')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customnewspost', models.ForeignKey(orm[u'news.customnewspost'], null=False)),
            ('deanery', models.ForeignKey(orm[u'tags.deanery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customnewspost_id', 'deanery_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'CustomNewsPost', fields ['slug', 'date']
        db.delete_unique(u'news_customnewspost', ['slug', 'date'])

        # Deleting model 'Category'
        db.delete_table(u'news_category')

        # Deleting model 'CustomNewsPost'
        db.delete_table(u'news_customnewspost')

        # Removing M2M table for field tags on 'CustomNewsPost'
        db.delete_table(db.shorten_name(u'news_customnewspost_tags'))

        # Removing M2M table for field secondary_tags on 'CustomNewsPost'
        db.delete_table(db.shorten_name(u'news_customnewspost_secondary_tags'))

        # Removing M2M table for field roles on 'CustomNewsPost'
        db.delete_table(db.shorten_name(u'news_customnewspost_roles'))

        # Removing M2M table for field deaneries on 'CustomNewsPost'
        db.delete_table(db.shorten_name(u'news_customnewspost_deaneries'))


    models = {
        u'assets.image': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Image'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.ImageCategory']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'assets.imagecategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ImageCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'authors.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'news.category': {
            'Meta': {'ordering': "(u'title',)", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'news.customnewspost': {
            'Meta': {'ordering': "(u'-date',)", 'unique_together': "((u'slug', u'date'),)", 'object_name': 'CustomNewsPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authors.Author']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['news.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'date_url': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'deaneries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Deanery']", 'symmetrical': 'False', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'hide_author': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'image_obj': ('cofeworcester.assets.fields.AssetForeignKey', [], {'to': u"orm['assets.Image']", 'null': 'True', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Role']", 'symmetrical': 'False', 'blank': 'True'}),
            'secondary_tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.SecondaryTag']", 'symmetrical': 'False', 'blank': 'True'}),
            'show_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'tags.deanery': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Deanery'},
            'acny_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'tags.role': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'tags.secondarytag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SecondaryTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'tags.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['news']