# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 21:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20160929_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 29, 21, 47, 11, 652492)),
            preserve_default=False,
        ),
    ]
