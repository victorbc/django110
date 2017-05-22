# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import shortner.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20170222_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortner.validators.validate_url, shortner.validators.validate_dot_com]),
        ),
    ]
