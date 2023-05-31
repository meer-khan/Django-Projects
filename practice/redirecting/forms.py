from django import forms 

class StudentRegistration(forms.Form):
    # initial argument can be given in forms.py aas well as views.py where we create object of this class
    # we give intial={} dictionary where we specify inital value of each field as key and value as value
    # we have done it app1
    # if we give inital values in both files, forms.py and views.py than what will happen? 
    # inital value of views.py will display on UI, because in views.py we are creating object of this class
    # and values given in the object has higher priority than given in class attributes
    # attrs={'autocomplete': 'off'}
    Name = forms.CharField()
    # email = forms.CharField(widget=forms.EmailField())
    Email= forms.EmailField(initial=None)
    # Email2= forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput(), initial=None)
    # Password = forms.PasswordInput()/
    # we can also remove PasswordInput() parenthesis, it will work fine like we did in below field of hiddenInput


    # password = forms.CharField(widget=forms.PasswordInput())
    # hiddenInput = forms.CharField(widget=forms.HiddenInput)
    # textArea = forms.CharField(widget=forms.Textarea)
    # checkbox = forms.CharField(widget=forms.CheckboxInput)
    # fileInput = forms.CharField(widget=forms.FileInput())


    # Attatching a custom attributes of HTML such as class with any field 


    # email = forms.CharField(widget=forms.EmailInput(attrs={"class": "email", "id":"uniqueID"}))