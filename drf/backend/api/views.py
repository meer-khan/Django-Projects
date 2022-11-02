from django.shortcuts import render
from django.http import JsonResponse
import json
from typing import Any
# from drf.backend.products import serializers
from products import models
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Items
from products.serializers import ItemsSerializer

# Create your views here.


@api_view(["GET"])
def api_home(request, *args, **kwargs):

    # Added ok
    # we can get the query parameters using the line below 
    print("GETTTTTTT",request.GET)

    # body = request.body
    # data = {}

    # we are using the try catch for the reason that when we dont have the data in the request
    # which means client doesnot send the data to the url 

    # try:
    #     data = json.loads(body)
    # except:
    #     pass

    # print(data.keys())
    # print (body) # that would be the byte string of json data that client is passing to us
    # return JsonResponse({'data':'hello this is my data'})



    # data['headers'] = request.headers
    # this above line give error of "Headers are not JSON seariable" which means
    # which means it's not the python dictionary and its could be the datatype of 
    # <class 'django.http.request.HttpHeaders'> so the JsonResponse method in the return statement 
    # cannot convert it into the JSON 
    # So we need to make it the python dictionary before passing it to the JsonReponse method

    # print(type(request.headers))


    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # data['params'] = request.GET
    # print(data)


# This line below get any random data from the Database and returns it back

    # model_data = models.Items.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
    #     data['title'] = model_data.title
    #     data['content'] = model_data.desc
    #     data['price'] = model_data.price

    # if request.method != "GET": 
    #     return Response({"Detail:":"POST is not allowed"}, status = 405)

    # Conversion of Django Model query response in the Python Dictionary using model_to_dict method of django 
    # data = {}
    # instance = models.Items.objects.all().order_by("?").first()
    # if instance:
        
    #     # data = model_to_dict(model_data)

    #     # data = model_to_dict(model_data, fields=['id' , 'title','desc','price'])


    #     data = ItemsSerializer(instance).data
    #     print(data)
    # return Response(data)



    # We were getting data from the DB and then pass it to the item
    # serlializer class and then serializer class does it's task 
    # What if we get data from the API and then pass it to the 
    # serializer and then dump the data into DB 



    data = request.data
    serializer = ItemsSerializer(data=data)
    if serializer.is_valid():
        instance = serializer.save()
    # in the DRF we use Response method instead of JsonResponse
    print(serializer.data)
    return Response(data)
