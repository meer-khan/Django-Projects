from django import forms 

class StudentRegistration(forms.Form):
    # initial argument can be given in forms.py aas well as views.py where we create object of this class
    # we give intial={} dictionary where we specify inital value of each field as key and value as value
    name = forms.CharField(label="Your Name", label_suffix='--',initial="Shahmeer",
                            required=False,disabled=True,help_text="70 Characters")