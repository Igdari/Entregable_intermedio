from django import forms

class PlanForm(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Costo = forms.FloatField()