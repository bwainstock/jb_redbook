import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Prediction(models.Model):

    prediction_text = models.TextField(unique=True)
    prediction_date = models.DateField('date predicted', auto_now_add=True)
    deadline_date = models.DateField('date prediction comes true')
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.prediction_text

    def was_predicted_recently(self):
        return self.prediction_date >= datetime.date.today() - datetime.timedelta(days=1)

    was_predicted_recently.admin_order_field = 'prediction_date'
    was_predicted_recently.boolean = True
    was_predicted_recently.short_description = 'Recently predicted?'
	
