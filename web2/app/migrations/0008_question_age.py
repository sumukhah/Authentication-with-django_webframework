# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190118_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='age',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
