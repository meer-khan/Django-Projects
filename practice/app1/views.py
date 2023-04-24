from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_func(request):
    return HttpResponse("HELLO DJANGO")


def my_func2(request):
    var = "SHAHMEER KHAN"
    return HttpResponse(f"HELLO {var}")