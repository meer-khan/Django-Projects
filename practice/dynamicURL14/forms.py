from django import forms 
import re
from django.core import validators
# from .models import User

class StudentRegistration(forms.ModelForm):
    pass
    # * We can also add as it is form fields in ModelForm like we did in, when we inheretied our class from forms.Form
    # * Before Meta class we can add each field same as forms.Form
    # * No matter we have added fields and define characteristics like max_length etc in models.py but 
    # * Priority of these fields will be high than models.py as well as forms.py 's Meta class 
    # name = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={"placeholder": "Bhai Naam likh"}))
    # class Meta: 
    #     model = User
    #     # WE CAN REORDER THE FIELDS BY REORDERING THEM IN BELOW LIST
    #     fields = ["name", "email", "password"]
    #     labels = {"name": "Enter Name", "email": "Enter Email", "password": "Enter Pass"}
    #     help_text = {"name": "Enter Full Name", "email": "Enter Official Email", "password": "Enter Strong Password"}
    #     error_messages = {"name": {"required": "Name is cumpolsory"}}
    #     widgets = {"password": forms.PasswordInput(attrs={"placeholder":"Strong Password"}), 
    #                "name": forms.TextInput(attrs={"class":"nameClass", "placeholder":"Full Name"}),
    #                "email":forms.TextInput(attrs={"placeholder":"Email"})}



