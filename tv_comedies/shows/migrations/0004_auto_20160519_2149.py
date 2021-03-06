# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20160518_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='episode',
            name='writer',
        ),
        migrations.AddField(
            model_name='episode',
            name='writers',
            field=models.ManyToManyField(to='shows.Writer'),
        ),
    ]
