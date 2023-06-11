from django import forms 
import re
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        fields = ["name", "email", "password"]
    name = forms.CharField(error_messages={"required":"Enter Your Name"}, min_length=5,max_length=50)
    email = forms.EmailField(error_messages={"required":"Enter Your Email"})
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={"required":"Enter Your Password"})




