# Generated by Django 2.0 on 2018-08-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auv', '0008_remove_auv_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auv',
            name='update_frequency',
            field=models.FloatField(default=1, help_text='Update frequency in [Hz]'),
        ),
    ]
