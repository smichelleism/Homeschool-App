# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0003_auto_20171122_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='outcome',
            field=models.CharField(blank=True, choices=[('A', 'Adopted'), ('D', 'Deceased'), ('I', 'Intake'), ('R', 'Released'), ('O', 'Other')], max_length=1),
        ),
    ]
