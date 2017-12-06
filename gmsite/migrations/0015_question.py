# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmsite', '0014_auto_20171205_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
                ('answer', models.TextField(blank=True, null=True)),
                ('show', models.BooleanField(default=False)),
            ],
        ),
    ]
