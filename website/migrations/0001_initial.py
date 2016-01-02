# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='create',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.models.MyUserObject'),
        ),
    ]
