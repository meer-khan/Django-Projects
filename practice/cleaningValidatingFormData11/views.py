from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def cleaningValidatingFormData(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "cleaningValidatingFormData11/userregistration11.html", {"form":fm})