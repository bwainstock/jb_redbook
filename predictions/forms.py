from django import forms

class PredictionForm(forms.Form):
	prediction = forms.CharField()
	deadline = forms.DateField()
