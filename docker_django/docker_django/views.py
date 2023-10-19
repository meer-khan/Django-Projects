from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    #  return HttpResponse("<h1>HELLO DJANGO</h1>")
    return render(request, "index.html")