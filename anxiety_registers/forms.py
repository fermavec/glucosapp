from django import forms

from .models import Anxiety
from users.models import User

class AnxietyForm(forms.ModelForm):
    class Meta:
        model = Anxiety  
        fields = ['anxiety_level', 'panic_attack', 'notes']  

    anxiety_level = forms.IntegerField(
        required=True,
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'anxiety_level',
            'placeholder': 'Entre 1 y 10'
        })
    )

    panic_attack = forms.CheckboxInput()

    notes = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'notes'
        })
    )
