# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-25 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armyapp', '0005_issueregister_currentdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueregister',
            name='currentdate',
        ),
        migrations.AddField(
            model_name='issueregister',
            name='issuedate',
            field=models.DateField(null=True),
        ),
    ]
