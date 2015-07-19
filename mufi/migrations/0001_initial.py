# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 7, 18, 13, 17, 6, 900361, tzinfo=utc))),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('uri', models.CharField(max_length=500)),
                ('start_time', models.PositiveIntegerField(default=0)),
                ('state', models.PositiveSmallIntegerField(max_length=1, choices=[('1', 'video_loading'), ('2', 'video_loading_success'), ('3', 'video_loading_error'), ('4', 'sound_process'), ('5', 'sound_process_success'), ('6', 'sound_process_error'), ('6', 'sound_search'), ('6', 'sound_search_success'), ('6', 'sound_search_error')])),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 7, 18, 13, 17, 6, 901481, tzinfo=utc))),
                ('trash', models.BooleanField(default=False)),
                ('site', models.ForeignKey(to='mufi.Site')),
            ],
        ),
    ]
