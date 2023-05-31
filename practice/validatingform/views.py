from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def validatingform(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "validatingform/userregistration5.html", {"form":fm})