# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoitem', '0004_auto_20171113_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
