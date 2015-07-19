# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0003_auto_20150718_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
