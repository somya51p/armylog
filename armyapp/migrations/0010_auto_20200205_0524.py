# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-02-05 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0009_auto_20200125_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueregister',
            name='materialno',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='issueregister',
            name='nomenclature',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stock',
            name='materialno',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='nomenclature',
            field=models.CharField(max_length=50),
        ),
    ]
