# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20180530_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='server.Course'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='present_students',
            field=models.ManyToManyField(to='server.Student'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Venue'),
        ),
    ]
