# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0020_auto_20151217_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='active',
            field=models.CharField(default=b'1', max_length=1),
            preserve_default=True,
        ),
    ]
