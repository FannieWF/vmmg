# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmpzxx',
            name='ssdw',
            field=models.CharField(max_length=20, verbose_name='\u7533\u8bf7\u4eba\u5355\u4f4d'),
        ),
    ]
