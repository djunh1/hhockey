# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-08-16 23:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('PICKUP', 'Pick up Game'), ('MENS LEAGUE', 'Mens League')], default='PICKUP', max_length=15)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('ON', 'On'), ('MAYBE', 'Maybe'), ('No', 'No')], default='ON', max_length=15)),
                ('starttime', models.DateTimeField(default=django.utils.timezone.now)),
                ('frequency', models.IntegerField(choices=[(0, 'Once'), (1, 'Daily'), (7, 'Weekly'), (14, 'Biweekly')])),
                ('cost', models.DecimalField(decimal_places=2, default='0.0', max_digits=5)),
                ('duration', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('recurring', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_created', to=settings.AUTH_USER_MODEL)),
                ('playerlist', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('starttime',),
                'verbose_name': 'Game',
            },
        ),
        migrations.CreateModel(
            name='Rink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('map', models.ImageField(blank=True, null=True, upload_to='')),
                ('gmap_url', models.CharField(blank=True, max_length=200, null=True)),
                ('skatesharpen', models.BooleanField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Rink',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='rink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gametime.Rink'),
        ),
    ]
