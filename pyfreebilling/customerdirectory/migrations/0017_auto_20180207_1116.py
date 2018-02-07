# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import pyfreebilling.customerdirectory.models


class Migration(migrations.Migration):

    dependencies = [
        ('customerdirectory', '0016_auto_20170522_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdirectory',
            name='password',
            field=models.CharField(blank=True, default=pyfreebilling.customerdirectory.models.random_string, help_text="It's recommended to use strong\n                                passwords for the endpoint.", max_length=100, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='customerdirectory',
            name='registration',
            field=models.BooleanField(default=True, help_text='Is registration needed\n                                       for calling ? True, the phone needs to\n                                       register with correct username/password.\n                                       If false, you must specify a CIDR in SIP\n                                       IP CIDR !', verbose_name='Registration'),
        ),
    ]
