# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import god.custom.myfield


class Migration(migrations.Migration):

    dependencies = [
        ('god', '0004_game_black_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '\u5df2\u4e0a\u7ebf'), (1, '\u5df2\u4e0b\u7ebf')], default=0, verbose_name='\u9879\u76ee\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='game',
            name='black_list',
            field=god.custom.myfield.ListField(),
        ),
    ]
