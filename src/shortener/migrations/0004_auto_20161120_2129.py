# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_kirrurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
