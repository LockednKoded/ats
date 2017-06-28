from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first name', 'last name']

        labels = {
            'username': 'User Name',
            'password': 'Password',
            'email': 'Email',
            'first name': 'First Name',
            'last name': 'Last Name'
        }


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            'username': 'User Name',
            'password': 'Password',
        }
