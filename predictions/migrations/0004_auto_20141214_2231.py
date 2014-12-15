# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_auto_20141214_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='prediction_text',
            field=models.TextField(unique=True),
            preserve_default=True,
        ),
    ]
