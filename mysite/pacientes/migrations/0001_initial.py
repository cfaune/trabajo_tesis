# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_ficha', models.IntegerField(unique=True)),
                ('rut', models.CharField(unique=True, max_length=30)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('fecha_ingreso', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
                ('cobertura', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='prevision',
            field=models.ForeignKey(to='pacientes.Prevision'),
        ),
    ]
