# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dining', '0003_auto_20161130_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='desc_delivery',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='desc_parking',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='operation_hour',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='review_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='total_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurantimg',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dining.Restaurant'),
        ),
    ]
