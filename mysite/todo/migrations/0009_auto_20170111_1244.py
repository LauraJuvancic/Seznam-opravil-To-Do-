# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_auto_20170110_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='arrival',
            field=models.DateField(help_text=None),
        ),
        migrations.AlterField(
            model_name='travel',
            name='departure',
            field=models.DateField(help_text=None),
        ),
        migrations.AlterField(
            model_name='travel',
            name='name',
            field=models.CharField(help_text=None, max_length=50),
        ),
    ]
