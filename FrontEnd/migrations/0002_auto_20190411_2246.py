# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-12 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontEnd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalresultadoheader',
            name='documentos',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='resultadoheader',
            name='documentos',
        ),
        migrations.AddField(
            model_name='resultadoheader',
            name='documentos',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
