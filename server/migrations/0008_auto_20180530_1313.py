# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20180530_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('radius', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='position',
        ),
        migrations.AddField(
            model_name='attendance',
            name='venue',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='server.Venue'),
            preserve_default=False,
        ),
    ]
