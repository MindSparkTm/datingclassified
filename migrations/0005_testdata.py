# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-15 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plentyofcats', '0004_auto_20180615_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Series_reference', models.CharField(blank=True, max_length=1000, null=True)),
                ('Period', models.CharField(blank=True, max_length=1000, null=True)),
                ('Data_value', models.CharField(blank=True, max_length=1000, null=True)),
                ('STATUS', models.CharField(blank=True, max_length=1000, null=True)),
                ('UNITS', models.CharField(blank=True, max_length=1000, null=True)),
                ('Subject', models.CharField(blank=True, max_length=1000, null=True)),
                ('Group', models.CharField(blank=True, max_length=1000, null=True)),
                ('Series_title_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('Series_title_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('Series_title_3', models.CharField(blank=True, max_length=1000, null=True)),
                ('Series_title_4', models.CharField(blank=True, max_length=1000, null=True)),
                ('Series_title_5', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
