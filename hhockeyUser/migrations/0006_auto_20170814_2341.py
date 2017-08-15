# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-08-14 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhockeyUser', '0005_remove_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='league',
            field=models.CharField(blank=True, choices=[('HOUSE LEAGUE', 'House League'), ('TRAVEL LEAGUE', 'Travel League'), ('JUNIORS', 'Juniors'), ('COLLEGE', 'College'), ('MAJOR JUNIORS', 'Major Juniors'), ('PROFESSIONAL', 'Professional'), ('REC LEAGUE', 'Rec League')], max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, choices=[('WING', 'Wing'), ('CENTER', 'Center'), ('DEFENSE', 'Defense'), ('GOALIE', 'Goalie')], max_length=8),
        ),
    ]
