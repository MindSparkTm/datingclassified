# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-15 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plentyofcats', '0006_auto_20180615_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdata',
            name='Series_title_2',
        ),
        migrations.RemoveField(
            model_name='testdata',
            name='Series_title_3',
        ),
        migrations.RemoveField(
            model_name='testdata',
            name='Series_title_4',
        ),
        migrations.RemoveField(
            model_name='testdata',
            name='Series_title_5',
        ),
    ]
