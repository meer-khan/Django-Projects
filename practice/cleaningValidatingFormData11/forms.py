from django import forms 

class StudentRegistration(forms.Form):

    name = forms.CharField()


    # we can also remove PasswordInput() parenthesis, it will work fine like we did in below field of hiddenInput


    # password = forms.CharField(widget=forms.PasswordInput())
    # hiddenInput = forms.CharField(widget=forms.HiddenInput)
    # textArea = forms.CharField(widget=forms.Textarea)
    # checkbox = forms.CharField(widget=forms.CheckboxInput)
    # fileInput = forms.CharField(widget=forms.FileInput())


    # Attatching a custom attributes of HTML such as class with any field 


    # email = forms.CharField(widget=forms.EmailInput(attrs={"class": "email", "id":"uniqueID"}))