# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-31 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='dataTime',
            new_name='dateTime',
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
