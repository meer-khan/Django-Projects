from django import forms 
import re
from django.core import validators




# def phone_num_starts_with_92(phno):
#     '''
#     This function is a custom validator
#     '''
#     # if phno[0] != '+':
#     #     raise forms.ValidationError("Number should start from +")
#     if not phno.startswith("+92"):
#         raise forms.ValidationError("Number should start from +92")

    

class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={"required":"Enter Your Name"}, min_length=5,max_length=50)
    email = forms.EmailField(error_messages={"required":"Enter Your Email"})
    password = forms.CharField(widget=forms.PasswordInput(),error_messages={"required":"Enter Your Password"})




