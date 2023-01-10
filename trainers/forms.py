from django import forms

class TrainerForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    free = forms.BooleanField(required=False)