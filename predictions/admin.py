from django.contrib import admin
from predictions.models import Prediction

# Register your models here.

class PredictionAdmin(admin.ModelAdmin):
    list_display= ('prediction_text', 'prediction_date', 'thumbs_up', 'thumbs_down', 'was_predicted_recently')
    list_filter = ['prediction_date', 'thumbs_up', 'thumbs_down', 'deadline_date']
    search_fields = ['prediction_text']

admin.site.register(Prediction, PredictionAdmin)
