# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0005_prediction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='user',
        ),
    ]
