# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitysearch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
