# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0008_auto_20150720_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='audio',
            field=models.ForeignKey(to='mufi.Audio', null=True),
        ),
    ]
