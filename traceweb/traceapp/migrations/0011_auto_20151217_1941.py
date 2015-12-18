# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0010_auto_20151214_0727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_id',
            new_name='des',
        ),
    ]
