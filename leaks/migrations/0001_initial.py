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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(null=True, blank=True, editable=False)),
                ('title', models.CharField(max_length=126, null=True, blank=True)),
                ('description', models.TextField()),
                ('rendered', models.TextField(null=True, blank=True, editable=False)),
                ('author', models.CharField(max_length=20, default='anon')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('metadata', models.TextField(null=True, default='', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags')),
            ],
        ),
    ]
