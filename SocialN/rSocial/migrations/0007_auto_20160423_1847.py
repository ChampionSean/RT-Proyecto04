# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rSocial', '0006_cometario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cometario',
            new_name='comentario',
        ),
    ]
