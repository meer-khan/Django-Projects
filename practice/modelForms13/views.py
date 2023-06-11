from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def modelForms(request):
    if request.method == "POST":

        fm = StudentRegistration(request.POST)
        print("THIS IS FM", fm)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            ps = fm.cleaned_data["password"]
            print("Name is: ", fm.cleaned_data.get("name"))
            print("Email is: ", fm.cleaned_data["email"])
            print("Password is: ", fm.cleaned_data["password"])

        
    else:
        fm = StudentRegistration()

    return render(request, "modelForms13/userregistration13.html", {"form":fm})