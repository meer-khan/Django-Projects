from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def formfieldtypes(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "formfieldtypes10/userregistration10.html", {"form":fm})