# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gammaukr', '0003_auto_20170706_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects_steps',
            name='text',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]