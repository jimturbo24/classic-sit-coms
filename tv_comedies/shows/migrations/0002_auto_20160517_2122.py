# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shows',
            new_name='Show',
        ),
    ]