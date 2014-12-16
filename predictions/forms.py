from django import forms
from django.forms.extras.widgets import SelectDateWidget

class PredictionForm(forms.Form):
	prediction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
#	deadline = forms.DateField(widget=SelectDateWidget)
        deadline = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}), required=True)
