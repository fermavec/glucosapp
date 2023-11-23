# forms.py
from django import forms
from .models import FoodInformation

class SearchForm(forms.Form):
    classification = forms.CharField(label='Clasificación', required=False)
    food = forms.CharField(label='Comida', required=False)
