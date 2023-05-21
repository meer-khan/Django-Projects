from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def forloop(request):
    fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "looponformandhiddenfields/userregistration2.html", {"forms":fm})