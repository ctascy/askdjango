# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
    ]
