# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-06 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0019_auto_20180207_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cb_currency',
        ),
        migrations.RemoveField(
            model_name='providertariff',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='ratecard',
            name='currency',
        ),
    ]
