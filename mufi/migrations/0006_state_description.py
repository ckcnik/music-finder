# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0005_auto_20150718_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='description',
            field=models.CharField(max_length=500, default=0),
            preserve_default=False,
        ),
    ]
