# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0011_homeschoolapplication_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitten',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unknown')], default='U', max_length=1, null=True),
        ),
    ]