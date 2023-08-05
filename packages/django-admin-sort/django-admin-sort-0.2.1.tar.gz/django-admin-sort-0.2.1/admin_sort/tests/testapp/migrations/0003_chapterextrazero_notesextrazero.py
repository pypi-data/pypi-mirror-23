# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20170503_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterExtraZero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Title')),
                ('my_order', models.PositiveIntegerField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.SortableBook')),
            ],
            options={
                'ordering': ('my_order', '-title'),
            },
        ),
        migrations.CreateModel(
            name='NotesExtraZero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('another_field', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Note2')),
                ('my_order', models.PositiveIntegerField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.SortableBook')),
            ],
            options={
                'ordering': ('my_order', 'another_field'),
            },
        ),
    ]
