# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-28 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhockeyUser', '0003_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
