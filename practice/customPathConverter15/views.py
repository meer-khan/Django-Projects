from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import HttpResponse

# Create your views here.


def customDynamicURL(request):
    # def app2_func(request):
    return HttpResponse("Hello in APP-2")


def show_details(request,year):
    student= {'yr':year}
    return render(request,'customPathConverter15/show.html', student)
