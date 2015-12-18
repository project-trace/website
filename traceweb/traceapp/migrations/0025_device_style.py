# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0024_auto_20151217_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='style',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
