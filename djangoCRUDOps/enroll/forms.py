from django import forms
from .models import User

# we donot perform validations in forms.py but I have imported this package 
from django.core import validators




class StudentRegistration(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            "name": forms.TextInput(attrs = {'class':'form-control' }),
            "email": forms.EmailInput(attrs = {'class':'form-control' }),
            # render_value = True will return the value of password when we are going on the edit page if we disable it, then 
            # django will not return us password but return us all other fields
            "password": forms.PasswordInput(attrs = {'class':'form-control' }, render_value=True)


        }