# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-03 07:36
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('djangocms_googlemap', '0008_removed_null_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlemapmarker',
            name='icon',
            field=filer.fields.image.FilerImageField(blank=True, help_text='A marker icon identifies a location on a map. By default, it uses a standard image from Google.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.Image', verbose_name='Icon'),
        ),
    ]
