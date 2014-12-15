from django import forms
from django.forms.extras.widgets import SelectDateWidget

class PredictionForm(forms.Form):
	prediction = forms.CharField()
#	deadline = forms.DateField(widget=SelectDateWidget)
        deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
