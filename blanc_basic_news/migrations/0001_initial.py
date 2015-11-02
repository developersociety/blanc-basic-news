# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique_for_date='date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('date_url', models.DateField(db_index=True, editable=False)),
                ('teaser', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('published', models.BooleanField(help_text='Post will be hidden unless this option is selected', default=True, db_index=True)),
                ('category', models.ForeignKey(to='news.Category')),
                ('image', blanc_basic_assets.fields.AssetForeignKey(to='assets.Image', null=True, blank=True)),
            ],
            options={
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
            bases=(models.Model,),
        ),
    ]
