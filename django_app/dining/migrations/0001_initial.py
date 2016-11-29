# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('img', versatileimagefield.fields.VersatileImageField(upload_to='menu_imgs', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('can_parking', models.BooleanField()),
                ('desc_parking', models.CharField(max_length=100)),
                ('desc_delivery', models.CharField(max_length=100)),
                ('operation_hour', models.CharField(max_length=100)),
                ('review_count', models.IntegerField()),
                ('review_score', models.FloatField()),
                ('total_like', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_favor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', versatileimagefield.fields.VersatileImageField(upload_to='restaurant_imgs', verbose_name='RestaurantImage')),
                ('alt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', versatileimagefield.fields.VersatileImageField(upload_to='review_imgs', verbose_name='ReviewImage')),
                ('alt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_and_down', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dining.Review')),
            ],
        ),
    ]
