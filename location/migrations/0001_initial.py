# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20160807_1034'),
        ('weibousers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('poiid', models.CharField(db_index=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weibo_id', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('created', models.DateField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('weibo_img', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to=b'')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weibousers.WeiboUser')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
