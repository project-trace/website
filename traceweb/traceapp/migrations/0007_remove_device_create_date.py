# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0006_auto_20151214_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='create_date',
        ),
    ]
