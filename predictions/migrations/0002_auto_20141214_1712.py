# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='prediction',
            field=models.OneToOneField(to='predictions.Prediction'),
            preserve_default=True,
        ),
    ]
