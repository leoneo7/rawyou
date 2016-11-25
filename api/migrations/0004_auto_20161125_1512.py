# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161125_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='emotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='api.Emotion'),
        ),
        migrations.AlterField(
            model_name='track',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='api.User'),
        ),
    ]