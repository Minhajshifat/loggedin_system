from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class registeruser(UserCreationForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=[
             'username','first_name','last_name','email'
        ]
class changepassword(UserCreationForm):
    class Meta:
        model=User
        fields=[
             'username','first_name','last_name','email'
        ]