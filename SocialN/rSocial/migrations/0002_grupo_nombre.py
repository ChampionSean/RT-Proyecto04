# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rSocial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
    ]
