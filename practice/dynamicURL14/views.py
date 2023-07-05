from django.shortcuts import render
from .forms import StudentRegistration
# from .models import User
# Create your views here.

def dynamicURL(request,id):
    return render(request, "dynamicURL14/userregistration14.html",{"id":id})


# Paramter name should be same as the name given in the pathconverter variable in URL
def integerID(request,id):
    if id == 1:
        data = {"id":1, "name":"Muhammad"}
    
    if id == 2:
        data = {"id":2, "name":"Khan"}
    
    if id == 3:
        data = {"id":3, "name":"Shahmeer"}

    return render(request, "dynamicURL14/userregistration14.html",data)


def integerID(request,id,subid):
    if id == 1:
        data = {"id":1, "name":"Muhammad", "subid":subid}
    
    if id == 2:
        data = {"id":2, "name":"Khan", "subid":subid}
    
    if id == 3:
        data = {"id":3, "name":"Shahmeer", "subid":subid}

    return render(request, "dynamicURL14/userregistration14.html",data)

def home(request):
    return render(request, "dynamicURL14/home.html")