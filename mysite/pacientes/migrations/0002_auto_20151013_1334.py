# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
                ('descripcion', models.CharField(unique=True, max_length=255)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='situacion',
            field=models.ForeignKey(to='pacientes.Situacion'),
        ),
    ]
