# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-27 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='servicessecond',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
