# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0018_homeschoolapplication_inventory_loaned'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitten',
            name='source',
            field=models.CharField(blank=True, choices=[('K', 'Kitty Cadet'), ('P', 'Public'), ('V', 'Volunteer'), ('U', 'Unknown'), ('T', 'TNR')], default='U', max_length=1, null=True),
        ),
    ]