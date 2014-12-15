# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0002_auto_20141214_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='prediction',
        ),
        migrations.DeleteModel(
            name='Votes',
        ),
        migrations.AddField(
            model_name='prediction',
            name='thumbs_down',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prediction',
            name='thumbs_up',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
