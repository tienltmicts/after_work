from django import forms
import re
from django.contrib.auth.models import User
from backend.models import *
from django.core.exceptions import ObjectDoesNotExist
    
class LoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())
