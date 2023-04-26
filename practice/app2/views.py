from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_func(request):
    return HttpResponse("Hello in APP-2")
