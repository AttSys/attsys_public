# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20180526_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='server.Course'),
        ),
    ]