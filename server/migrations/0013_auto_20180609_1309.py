# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_attendance_mat_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='mat_no',
        ),
        migrations.AddField(
            model_name='student',
            name='mat_no',
            field=models.CharField(default='', max_length=10),
        ),
    ]