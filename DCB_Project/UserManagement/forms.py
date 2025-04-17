from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserChangeForm,SetPasswordForm,AuthenticationForm,PasswordChangeForm



class LoginForm(forms.Form):
    email_or_phone = forms.CharField(label='Email or Phone')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    