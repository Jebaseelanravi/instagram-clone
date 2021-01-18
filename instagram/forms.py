from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Username"},))
    first_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"First Name"}))
    last_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Last Name"}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-fields','placeholder':"Password"}),required=True)

