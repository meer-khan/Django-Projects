from django import forms 
import re
from django.core import validators




def phone_num_starts_with_92(phno):
    '''
    This function is a custom validator
    '''
    # if phno[0] != '+':
    #     raise forms.ValidationError("Number should start from +")
    if not phno.startswith("+92"):
        raise forms.ValidationError("Number should start from +92")

    

class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    # We are creating this field to reenter password and makes sure, both password match by using 
    # the clean() function, in clean function we write custom logic to check both passwords are same or not
    repassword = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    
    # * Writing Builtin validators: 
    '''
    CUSTOM VALIDATION FIELDS
    '''
    fullName = forms.CharField(validators=[validators.MaxLengthValidator(20), 
                                           validators.MinLengthValidator(5),])
    
    pho_no = forms.CharField(validators=[phone_num_starts_with_92])

    # def clean_name(self):
    '''
    This function is used to evaluate/validate the name field
    '''
    #     valName= self.cleaned_data["name"]
    #     # OR we can also write it as 
    #     # valName = self.cleaned_data.get("name")

    #     if len(valName) < 4: 
    #         raise forms.ValidationError("Enter more than 4 characters")
        
    #     # * Validatoin to check there is no special character in name using Regex
    #     pattern = r'^[a-zA-Z0-9 ]+$'  # Regular expression pattern to allow only alphanumeric characters and spaces

    #     # if not re.match(pattern, valName):
    #     #     raise forms.ValidationError("Name can only contain letters, numbers, and spaces.")
        
    #     # * We can also do this using isalnum() is alpha numeric function 
    #     for char in valName:
    #         if not char.isalnum():
    #             raise forms.ValidationError(f"Name can only contain letters, numbers, and spaces.you cannot add {char}")
            
        # return valName
    def clean(self):
        '''
        This function is to validate the complete form
        '''

        # we write below line to ensure that clean() class of django's validations also perfomed in our StudentRegistration Class
        # TODO: But code works without creating this object, So, it's little unclear concept right now
        cleaned_data = super().clean()
        valName = self.cleaned_data["name"]
        valEmail = self.cleaned_data.get("email")
        valNo = self.cleaned_data["pho_no"]
        valpass = self.cleaned_data["password"]
        revalpass = self.cleaned_data["repassword"]
        if revalpass != valpass:
            raise forms.ValidationError("Passwords does not match")

        if len(valName) < 4 : 
            raise forms.ValidationError("Enter Name with more than 4 character and make sure there is no special character in it")
        
        if len(valEmail)< 10 :
            raise forms.ValidationError("Email should not include less than 10 characters")
        

        
        # return valName



