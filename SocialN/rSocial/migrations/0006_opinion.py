# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-23 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rSocial', '0005_auto_20160420_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='opinion',
            fields=[
                ('id_opinion', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=500)),
                ('id_post_opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rSocial.post')),
            ],
        ),
    ]
