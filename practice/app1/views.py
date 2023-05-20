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
    # BY DEFAULT: auto_id attribute is "id_%s"
    # fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})


    #* CONFIGURE AUTO_ID

    # # BY DEFAULT: auto_id attribute is "id_%s" 
    # # if auto_id set to string that includes fromat character %s then form will display id as "whateverstring%s"
    # fm = StudentRegistration(auto_id="ANYSTRING_%s")
    # return render(request,'app1/userregistration.html', {"form":fm})


    # # if auto_id set to false then form output will not include <label> tag nor id attributes
    # fm = StudentRegistration(auto_id=False)
    # return render(request,'app1/userregistration.html', {"form":fm})

    # # if auto_id set to True then form output will include <label> tag and id attributes as name of the field
    # fm = StudentRegistration(auto_id=True)
    # return render(request,'app1/userregistration.html', {"form":fm})

    # # if auto_id set to anystring that does not include %s then form will act as auto_id is TRUE
    # fm = StudentRegistration(auto_id="ANYSTRING")
    # return render(request,'app1/userregistration.html', {"form":fm})


    #* CONFIGURE LABEL TAG
    # fm = StudentRegistration(label_suffix="-")
    # return render(request,'app1/userregistration.html', {"form":fm})


    #* CONFIGURE DYNAMIC INITIAL VALUES
    # fm = StudentRegistration(label_suffix="-", auto_id="myID_%s", initial={"name":"MEER","email": "KHAN"})
    # return render(request,'app1/userregistration.html', {"form":fm})


    #* ORDERING OF INPUT FIELDS
    fm = StudentRegistration(label_suffix="-", auto_id="myID_%s", initial={"name":"MEER","email": "KHAN"}, field_order=["email","name"])
    return render(request,'app1/userregistration.html', {"form":fm})