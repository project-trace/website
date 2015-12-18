# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0015_auto_20151217_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='img',
            field=models.CharField(default=b'static/traceapp/img/item.png', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
