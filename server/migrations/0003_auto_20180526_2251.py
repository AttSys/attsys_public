# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20180526_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
