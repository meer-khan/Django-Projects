from django.shortcuts import render
from django.http import HttpResponse


# Basic functional APIs
# Create your views here.
def index(request): 
    return HttpResponse("Home Page")

def my_func(request):
    return HttpResponse("HELLO DJANGO")


def my_func2(request):
    var = "SHAHMEER KHAN"
    return HttpResponse(f"HELLO {var}")