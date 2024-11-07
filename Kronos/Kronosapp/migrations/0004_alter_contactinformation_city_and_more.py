# Generated by Django 5.1.1 on 2024-10-16 23:39

import Kronosapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kronosapp', '0003_alter_schedules_tssid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='postalCode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='province',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contactinformation',
            name='streetNumber',
            field=models.CharField(blank=True, max_length=10, validators=[Kronosapp.models.validate_numeric]),
        ),
    ]
