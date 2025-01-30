from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter unique username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'example@gmail.com'}))
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Create trusty password'}))
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Create trusty password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter your username'}))
    password = forms.CharField(min_length=3, widget=forms.PasswordInput(
        attrs={'class': 'input', 'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class AddQuoteForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput())
    writer = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter a author name'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter a author name'}))

    class Meta:
        pass
