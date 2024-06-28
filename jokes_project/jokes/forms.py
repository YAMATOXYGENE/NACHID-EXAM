from django import forms
from django.contrib.auth.models import User
from .models import Joke

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer']
