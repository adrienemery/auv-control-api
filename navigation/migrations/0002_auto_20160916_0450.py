# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waypoint',
            old_name='lon',
            new_name='lng',
        ),
        migrations.AlterField(
            model_name='waypoint',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='navigation.Trip'),
        ),
    ]