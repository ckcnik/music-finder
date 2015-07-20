# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mufi', '0006_state_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('acrid', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('trash', models.BooleanField(default=False)),
                ('audio', models.ForeignKey(to='mufi.Audio')),
                ('video', models.ForeignKey(to='mufi.Video')),
            ],
        ),
    ]
