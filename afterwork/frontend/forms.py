import datetime
from django import forms
from django.contrib.auth.forms import User
from backend.models import *

class LoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",max_length=30,widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    position = forms.Select(choices=POSITION)
    level = forms.Select(choices=LEVEL_CHOICE)

class CommentForm(forms.Form):
    sender = forms.CharField(label="Sender", max_length=30)
    email = forms.CharField(label="Email",max_length=30)
    comment = forms.CharField(label="Comment",widget=forms.Textarea)

class UpdateProfileForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control form-control-alternative'
            }), max_length=255)
    email = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control form-control-alternative'
            }), max_length=255)
    birthday = forms.DateField(required=False, widget=forms.DateInput(
        attrs={
                'class': 'form-control form-control-alternative'
            }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control form-control-alternative'
            }), max_length=255)
    gender = forms.Select(choices=USER_PROFILE_GENDER_CHOICES)
    id_selfie = forms.ImageField(required=False)
    current_address = forms.CharField(widget=forms.Textarea(
        attrs={
                'class': 'form-control form-control-alternative'
            }), required=False)
    position = forms.Select(choices=POSITION)
    level = forms.Select(choices=LEVEL_CHOICE)
class RegisterSubjectsForm(forms.Form):
    pk = forms.IntegerField()
    name = forms.CharField(max_length=255)
    level = forms.CharField(max_length=255)

class FilterTKBForm(forms.Form):
    paradigm = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))