# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-30 15:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FrontEnd', '0005_auto_20190428_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalResultadoBusqInteligenteTokens',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('destacado', models.BooleanField()),
                ('aparicion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
                ('frase', models.CharField(max_length=150)),
                ('lema', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('parrafo_nro', models.IntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('doc', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FrontEnd.Documento')),
                ('header', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FrontEnd.ResultadoHeader')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parrafo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FrontEnd.Parrafo')),
            ],
            options={
                'verbose_name': 'historical resultado busq inteligente tokens',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTokensDoc',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('aparicion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
                ('frase', models.CharField(max_length=150)),
                ('lema', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('eliminado', models.BooleanField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('doc', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FrontEnd.Documento')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parrafo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='FrontEnd.Parrafo')),
            ],
            options={
                'verbose_name': 'historical tokens doc',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ResultadoBusqInteligenteTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destacado', models.BooleanField()),
                ('aparicion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
                ('frase', models.CharField(max_length=150)),
                ('lema', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('parrafo_nro', models.IntegerField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.Documento')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.ResultadoHeader')),
                ('parrafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.Parrafo')),
            ],
        ),
        migrations.CreateModel(
            name='TokensDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparicion', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
                ('frase', models.CharField(max_length=150)),
                ('lema', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('eliminado', models.BooleanField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.Documento')),
                ('parrafo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FrontEnd.Parrafo')),
            ],
        ),
        migrations.AlterField(
            model_name='caso',
            name='modelo',
            field=models.CharField(choices=[('ECON', 'Económico'), ('DRUG', 'Drogas')], default='ECON', max_length=10),
        ),
        migrations.AlterField(
            model_name='entidadesdoc',
            name='string',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='entidadesdoc',
            name='string_original',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalcaso',
            name='modelo',
            field=models.CharField(choices=[('ECON', 'Económico'), ('DRUG', 'Drogas')], default='ECON', max_length=10),
        ),
        migrations.AlterField(
            model_name='historicalentidadesdoc',
            name='string',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalentidadesdoc',
            name='string_original',
            field=models.CharField(max_length=100),
        ),
    ]
