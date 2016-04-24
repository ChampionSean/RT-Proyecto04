# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rSocial', '0005_auto_20160420_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='cometario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=150)),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rSocial.post')),
            ],
        ),
    ]
