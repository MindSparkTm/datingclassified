# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-20 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plentyofcats', '0011_userad_uploaded_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='userad',
            name='uploaded_file_url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
