from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def modelForms(request):
    if request.method == "POST":

        fm = StudentRegistration(request.POST)
        print("THIS IS FM", fm)
        # This try block is for email specifically, if we write email without @ or not with email format 
        # than Django server gives error that NoneType object has no method len()
        # Try except block catch the exception and than Django automatically prompts on webUI that 
        # Email should be in correct format 
        # This is not taught in lectures, I have explored it on my own 
        # try:
        if fm.is_valid():
            print("Name is: ", fm.cleaned_data.get("name"))
            print("Email is: ", fm.cleaned_data["email"])
        # except Exception as e: 
        #     print(e) 
    else:
        fm = StudentRegistration()
    
    # fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})

    return render(request, "modelForms13/userregistration13.html", {"form":fm})