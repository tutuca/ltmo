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
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True, max_length=1024)),
                ('clicks', models.PositiveIntegerField(blank=True, default=0)),
                ('views', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateBanner',
            fields=[
                ('banner_ptr', models.OneToOneField(parent_link=True, to='banners.Banner', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(upload_to='banners', null=True)),
                ('url', models.URLField(blank=True)),
                ('template', models.CharField(default='banner.html', max_length=70)),
            ],
            bases=('banners.banner',),
        ),
        migrations.AddField(
            model_name='banner',
            name='slot',
            field=taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.'),
        ),
    ]
