# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURLManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
