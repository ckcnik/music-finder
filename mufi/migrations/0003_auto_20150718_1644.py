# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0002_auto_20150718_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[('1', 'video_loading'), ('2', 'video_loading_success'), ('3', 'video_loading_error'), ('4', 'sound_process'), ('5', 'sound_process_success'), ('6', 'sound_process_error'), ('7', 'sound_search'), ('8', 'sound_search_success'), ('9', 'sound_search_error')]),
        ),
    ]
