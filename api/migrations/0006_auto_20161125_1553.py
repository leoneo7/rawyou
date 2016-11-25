# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20161125_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='emotion_name',
            new_name='emotion_id',
        ),
        migrations.AlterField(
            model_name='track',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
    ]
