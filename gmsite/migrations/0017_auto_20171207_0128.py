# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 23:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmsite', '0016_projects_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 7, 1, 28, 10, 158939)),
        ),
    ]