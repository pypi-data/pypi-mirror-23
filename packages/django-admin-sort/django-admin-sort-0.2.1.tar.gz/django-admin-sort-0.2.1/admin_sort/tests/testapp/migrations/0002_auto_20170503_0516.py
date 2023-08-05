# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='another_field',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Note2'),
        ),
        migrations.AddField(
            model_name='notes',
            name='one_more',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Note3 (simulating tabular inlines)'),
        ),
    ]
