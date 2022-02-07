from django import forms

class CalcImcForm(forms.Form):
    peso = forms.CharField(
        required=False)
    altura = forms.CharField(
        required=False)