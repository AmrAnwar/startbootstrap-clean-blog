# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 16:45
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]