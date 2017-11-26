# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs', '0012_kitten_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitten',
            name='outcome',
            field=models.CharField(blank=True, choices=[('P', 'In HS Program'), ('A', 'Adopted'), ('D', 'Deceased'), ('E', 'Escaped'), ('F', 'Foster Fail Adoption'), ('I', 'Intake'), ('R', 'Released'), ('T', 'TIAA'), ('O', 'Other')], max_length=1, null=True),
        ),
    ]
