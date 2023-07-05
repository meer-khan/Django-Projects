from django import forms
from .models import User

# we donot perform validations in forms.py but I have imported this package 
from django.core import validators




class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['name', 'email', 'password']