# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20151013_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='fecha_diagnostico',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 13, 51, 25, 575927, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
