from django import forms
from clients.models import Clients

class ClientForm(forms.Form):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=300)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()

