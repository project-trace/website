# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0022_auto_20151217_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='enabled',
            field=models.CharField(default=b'Enable', max_length=1),
            preserve_default=True,
        ),
    ]
