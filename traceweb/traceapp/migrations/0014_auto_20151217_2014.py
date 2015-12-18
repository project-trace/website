# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceapp', '0013_auto_20151217_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='img',
            field=models.CharField(default=b'static/traceapp/img/keys.png', max_length=200),
            preserve_default=True,
        ),
    ]
