# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0017_homeschoolapplication_donations_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeschoolapplication',
            name='inventory_loaned',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]