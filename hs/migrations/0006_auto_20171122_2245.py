# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0005_homeschoolapplication_rescue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeschoolapplication',
            name='hh_income',
            field=models.CharField(blank=True, choices=[('24', '24,000 or Below'), ('35', 'Between 24,000 and 35,000'), ('65', 'Between 35,000 and 65,000'), ('99', 'Above 65,000')], max_length=2, verbose_name='What is your household income?'),
        ),
    ]