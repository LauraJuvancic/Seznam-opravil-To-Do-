# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
