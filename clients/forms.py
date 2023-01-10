from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()