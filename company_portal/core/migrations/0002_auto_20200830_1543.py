# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-30 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='created_at',
            field=models.CharField(max_length=100),
        ),
    ]
