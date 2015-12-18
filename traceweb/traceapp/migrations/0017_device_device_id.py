# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0016_auto_20151217_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
