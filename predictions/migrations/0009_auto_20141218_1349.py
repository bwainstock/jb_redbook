# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictions', '0008_prediction_up_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='down_votes',
            field=models.ManyToManyField(related_name='prediction_down', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prediction',
            name='up_votes',
            field=models.ManyToManyField(related_name='prediction_up', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
