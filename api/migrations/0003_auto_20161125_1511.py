# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161125_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='emotion_id',
            new_name='emotion',
        ),
        migrations.RenameField(
            model_name='track',
            old_name='user_id',
            new_name='user',
        ),
    ]