# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0007_audio_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='play_offset',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='response',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
