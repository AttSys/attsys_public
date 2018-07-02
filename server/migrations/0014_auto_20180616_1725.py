# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_auto_20180609_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Student')),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='present_students',
            field=models.ManyToManyField(blank=True, to='server.StudentRecord'),
        ),
    ]