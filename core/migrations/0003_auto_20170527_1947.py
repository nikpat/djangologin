# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170527_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='country',
        ),
    ]
