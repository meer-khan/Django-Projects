from django import forms 
import re
class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_name(self):
        valName= self.cleaned_data["name"]
        # OR we can also write it as 
        # valName = self.cleaned_data.get("name")

        if len(valName) < 4: 
            raise forms.ValidationError("Enter more than 4 characters")
        
        # * Validatoin to check there is no special character in name using Regex
        pattern = r'^[a-zA-Z0-9 ]+$'  # Regular expression pattern to allow only alphanumeric characters and spaces

        # if not re.match(pattern, valName):
        #     raise forms.ValidationError("Name can only contain letters, numbers, and spaces.")
        
        # * We can also do this using isalnum() is alpha numeric function 
        for char in valName:
            if not char.isalnum():
                raise forms.ValidationError(f"Name can only contain letters, numbers, and spaces.you cannot add {char}")
            
        return valName
    def clean(self):
        '''
        This function is to validate the complete form
        '''
        cleaned_data = super().clean()
        valName = self.cleaned_data.get("name")
        if valName < 4 : 
            raise forms.ValidationError("Enter Name with more than 4 character and make sure there is no special character in it")
        
        return valName


