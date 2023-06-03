from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def cleaningValidatingFormData(request):
    if request.method == "POST":

        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Name is: ", fm.cleaned_data.get("name"))
            print("Email is: ", fm.cleaned_data["email"])
    else:
        fm = StudentRegistration()
        
    # return render(request,'app1/userregistration.html', {"form":fm})

    return render(request, "cleaningValidatingFormData11/userregistration11.html", {"form":fm})