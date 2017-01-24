# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20170118_1425'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShortURLManager',
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]