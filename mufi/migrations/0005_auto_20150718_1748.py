# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0004_auto_20150718_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.ForeignKey(to='mufi.State'),
        ),
    ]
