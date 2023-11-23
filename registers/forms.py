from django import forms

from readings.models import Reading  # Asegúrate de importar el modelo correcto
from users.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Reading  # Asocia el formulario con el modelo Reading
        fields = ['reading_value', 'category', 'notes']  # Especifica los campos que deseas incluir en el formulario

    reading_value = forms.DecimalField(
        required=True,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'reading_value',
            'placeholder': 'Lectura'
        })
    )

    #category = 1

    notes = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'notes',
            'placeholder': 'Notas adicionales'
        })
    )
