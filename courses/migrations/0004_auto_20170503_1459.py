# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150601_1513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step',
            new_name='Text',
        ),
    ]
