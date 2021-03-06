# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmsite', '0009_auto_20171202_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicessecondpricetableelement',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='servicessecondpricetableelement',
            name='news',
        ),
        migrations.RemoveField(
            model_name='servicessecondpricetableelement',
            name='project',
        ),
        migrations.AddField(
            model_name='servicessecondcontent',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gmsite.Gallery'),
        ),
        migrations.AddField(
            model_name='servicessecondcontent',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gmsite.News'),
        ),
        migrations.AddField(
            model_name='servicessecondcontent',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gmsite.Projects'),
        ),
    ]
