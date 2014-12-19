# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0006_remove_prediction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='thumbs_down',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='thumbs_up',
        ),
    ]
