from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from .forms import StudentRegistration
# Basic functional APIs
# Create your views here.

# first API
def index(request): 
    return HttpResponse("Home Page")

def my_func(request):
    return HttpResponse("HELLO DJANGO")


def my_func2(request):
    var = Student.objects.all()
    print(var[0].student_name)
    print(list(var.values()))
    
    return HttpResponse(f"HELLO {list(var.values())}, NAME: {var[0].student_name}, Address: {var[0].student_address}")


def show_forms_data(request):
    fm = StudentRegistration()
    return render(request,'app1/userregistration.html', {"form":fm})
