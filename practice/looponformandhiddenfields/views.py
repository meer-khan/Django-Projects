from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def formloop(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "looponformandhiddenfields/userregistration2.html", {"form":fm})