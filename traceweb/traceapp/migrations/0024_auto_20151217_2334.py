# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0023_auto_20151217_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='button',
            field=models.CharField(default=b'Disable', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='enabled',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
    ]
