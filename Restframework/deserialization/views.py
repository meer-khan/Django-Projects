from django.shortcuts import render
from serialization.models import Student
from .serializers import StudentSerializer
import io
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.

@csrf_exempt
def student_create(request):
    # * In Django 4.0, the handling of JSON data has been improved, and you typically don't need to manually convert 
    # * JSON data from bytes to a string and then to a Python dictionary. 
    # * Django's built-in JSON support takes care of parsing the JSON data for you.
    # * But Geekyshows is working on Django 3 so he's doing io stream 
    # * Check Docs (My word doc) for further explanation

    if request.method == "POST":
        # print(request.data)
        # jsonData = request.body
        # print("Data from body: ", jsonData)
        # print(type(jsonData))

        jsonData = json.loads(request.body)

        print("Data from data: ", jsonData)
        print(type(jsonData))
        
        # * Data parameter is for all the post requests - Remember this point 
        serializer = StudentSerializer(data =jsonData)
        if serializer.is_valid():
            serializer.save()
        
            return JsonResponse(data={'msg': 'Registration Successful '})
        print("data not valid")
        return JsonResponse(data={'msg': 'Registration not Successful '})




# * API LIKE DJango 3 Requirements

# @csrf_exempt
# def student_create(request):
#     # * In Django 4.0, the handling of JSON data has been improved, and you typically don't need to manually convert 
#     # * JSON data from bytes to a string and then to a Python dictionary. 
#     # * Django's built-in JSON support takes care of parsing the JSON data for you.
#     # * But Geekyshows is working on Django 3 so he's doing io stream 
#     # * Check Docs (My word doc) for further explanation

#     if request.method == "POST":
#         jsonData = request.body
#         stream = io.BytesIO(jsonData)
#         pythonData =JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythonData)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(JSONRenderer().render(data={'msg': 'Registration Successful '}))
#             # return JsonResponse(data={'msg': 'Registration Successful '})
#         print("data not valid")
#         return JsonResponse(data={'msg': 'Registration not Successful '})