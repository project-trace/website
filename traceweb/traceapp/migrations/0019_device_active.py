# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0018_auto_20151217_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
