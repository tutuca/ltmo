# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20141128_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('slug', models.SlugField(blank=True, null=True, editable=False)),
                ('title', models.CharField(blank=True, max_length=126, null=True)),
                ('description', models.TextField()),
                ('rendered', models.TextField(blank=True, null=True, editable=False)),
                ('author', models.CharField(max_length=20, default='anon')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('metadata', models.TextField(blank=True, default='', null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
        ),
    ]
