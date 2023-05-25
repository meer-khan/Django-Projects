from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()