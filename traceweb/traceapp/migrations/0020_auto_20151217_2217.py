# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0019_device_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
