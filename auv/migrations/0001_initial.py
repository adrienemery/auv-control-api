# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AUV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50, unique=True)),
                ('last_seen', models.DateTimeField(blank=True, help_text='updated whenever a heartbeat is recieved', null=True)),
                ('max_depth', models.FloatField(blank=True, null=True)),
                ('max_speed', models.FloatField(blank=True, null=True)),
                ('max_time_underwater', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AUVData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('battery_percentage', models.FloatField(blank=True, null=True)),
                ('battery_temperature', models.FloatField(blank=True, null=True)),
                ('depth', models.FloatField(blank=True, null=True)),
                ('speed', models.FloatField(blank=True, null=True)),
                ('heading', models.FloatField(blank=True, null=True)),
                ('roll', models.FloatField(blank=True, null=True)),
                ('pitch', models.FloatField(blank=True, null=True)),
                ('yaw', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('auv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auv.AUV')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
