# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20161128_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access_token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
