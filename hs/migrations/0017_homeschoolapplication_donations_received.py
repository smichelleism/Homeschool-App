# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0016_merge_20171201_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeschoolapplication',
            name='donations_received',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
