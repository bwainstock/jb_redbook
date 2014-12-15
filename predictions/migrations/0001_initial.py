# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prediction_text', models.TextField()),
                ('prediction_date', models.DateField(auto_now_add=True, verbose_name=b'date predicted')),
                ('deadline_date', models.DateField(verbose_name=b'date prediction comes true')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbs_up', models.IntegerField(default=0)),
                ('thumbs_down', models.IntegerField(default=0)),
                ('prediction', models.ForeignKey(to='predictions.Prediction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
