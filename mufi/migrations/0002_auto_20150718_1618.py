# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='video',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[('1', 'video_loading'), ('2', 'video_loading_success'), ('3', 'video_loading_error'), ('4', 'sound_process'), ('5', 'sound_process_success'), ('6', 'sound_process_error'), ('6', 'sound_search'), ('6', 'sound_search_success'), ('6', 'sound_search_error')]),
        ),
    ]
