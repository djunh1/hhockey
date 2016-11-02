# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='oauth_secret',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='oauth_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='league',
            field=models.CharField(blank=True, choices=[('HOUSE LEAGUE', 'House League'), ('TRAVEL LEAGUE', 'Travel League'), ('JUNIORS', 'Juniors'), ('COLLEGE', 'College'), ('MAJOR JUNIORS', 'Major Juniors'), ('PROFESSIONAL', 'Professional')], max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('WING', 'Wing'), ('CENTER', 'Center'), ('DEFENSE', 'Defense')], max_length=8),
        ),
    ]