# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('presents', models.TextField()),
                ('alarm', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('ingredients', models.TextField()),
                ('procedure', models.TextField()),
                ('alarm', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('info', models.TextField()),
                ('alarm', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('info', models.TextField()),
                ('alarm', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('stuff', models.TextField()),
                ('alarm', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('category', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date1', models.DateTimeField()),
                ('date2', models.DateTimeField()),
                ('destination', models.DateTimeField(max_length=100)),
                ('pack', models.TextField()),
                ('info', models.TextField()),
                ('alarm', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('info', models.TextField()),
                ('mails', models.EmailField(max_length=254)),
                ('workers', models.TextField()),
                ('alarm', models.BooleanField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks')),
            ],
        ),
        migrations.AddField(
            model_name='shopping',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks'),
        ),
        migrations.AddField(
            model_name='personal',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks'),
        ),
        migrations.AddField(
            model_name='home',
            name='taks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks'),
        ),
        migrations.AddField(
            model_name='cooking',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks'),
        ),
        migrations.AddField(
            model_name='birthday',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Tasks'),
        ),
    ]