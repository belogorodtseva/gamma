# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmsite', '0015_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
