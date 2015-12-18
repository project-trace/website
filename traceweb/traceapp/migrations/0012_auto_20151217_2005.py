# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0011_auto_20151217_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='img',
            field=models.CharField(default=b'/traceapp/img/item.png', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='des',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
