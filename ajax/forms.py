from django import forms

from ajax.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'