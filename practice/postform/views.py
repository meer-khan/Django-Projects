from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def postform(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "postform/userregistration4.html", {"form":fm})