# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_course_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='mat_no',
            field=models.CharField(default='', max_length=10),
        ),
    ]
