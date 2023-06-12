from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

def dynamicURL(request):
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
            obj = User(name = nm, email = em, password = ps)
            obj.save()

        
    else:
        fm = StudentRegistration()

    return render(request, "dynamicURL14/userregistration14.html", {"form":fm})