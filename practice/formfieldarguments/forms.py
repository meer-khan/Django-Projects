from django import forms 

class StudentRegistration(forms.Form):
    # initial argument can be given in forms.py aas well as views.py where we create object of this class
    # we give intial={} dictionary where we specify inital value of each field as key and value as value
    # we have done it app1
    # if we give inital values in both files, forms.py and views.py than what will happen? 
    # inital value of views.py will display on UI, because in views.py we are creating object of this class
    # and values given in the object has higher priority than given in class attributes
    name = forms.CharField(label="Your Name", label_suffix='--',initial="Shahmeer",
                            required=False,disabled=True,help_text="70 Characters")