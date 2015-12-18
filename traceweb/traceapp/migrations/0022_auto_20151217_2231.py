# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0021_auto_20151217_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='active',
            new_name='enabled',
        ),
    ]
