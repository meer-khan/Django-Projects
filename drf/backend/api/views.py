from django.shortcuts import render
from django.http import JsonResponse
import json
from typing import Any
from products import models

# Create your views here.

def api_home(request, *args, **kwargs):


    # we can get the query parameters using the line below 
    # print(request.GET)

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


    model_data = models.Items.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.desc
        data['price'] = model_data.price
    return JsonResponse(data)
