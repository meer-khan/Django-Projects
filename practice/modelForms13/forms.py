from django import forms 
import re
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        # WE CAN REORDER THE FIELDS BY REORDERING THEM IN BELOW LIST
        fields = ["name", "email", "password"]
        labels = {"name": "Enter Name", "email": "Enter Email", "password": "Enter Pass"}
        help_text = {"name": "Enter Full Name", "email": "Enter Official Email", "password": "Enter Strong Password"}
        error_messages = {"name": {"required": "Name is cumpolsory"}}
        widgets = {"password": forms.PasswordInput(attrs={"placeholder":"Strong Password"}), 
                   "name": forms.TextInput(attrs={"class":"nameClass", "placeholder":"Full Name"}),
                   "email":forms.TextInput(attrs={"placeholder":"Email"})}



