# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoitem', '0003_auto_20171113_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(max_length=6),
        ),
    ]
