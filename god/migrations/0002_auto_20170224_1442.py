# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('god', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dbbackup',
            table='dbBackup',
        ),
    ]
