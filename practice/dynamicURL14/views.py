from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

def dynamicURL(request,id):
    

    return render(request, "dynamicURL14/userregistration14.html",{"id":id})