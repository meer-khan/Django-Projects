from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Serialization and Json conversion of Model Instance 
def student_detail(request):
    stu = Student.objects.get(id = 1)
    # print(type(stu))
    serializer = StudentSerializer(stu)
    print(type(serializer.data))




    # * we donot need to write these two lines if we are using JsonResponse Class

    jsonData = JSONRenderer().render(serializer.data)
    print(jsonData)
    print(type(jsonData))
    return HttpResponse(jsonData)


    # * we wrote two lines, 1 is to convert serialized data into json using JSONRenderer() and 
    # * 2 is to send it back to the api using HTTPResponse()

    # we can achieve the same task in single line using JsonResponse class of rest_framework

    # if the safe parameter is set to true (BY DEFAULT) then JsonResponse will only take dictionary of key value pairs 
    # but if we want to send list of dictionaries we need to set the safe parameter as False
    return JsonResponse(serializer.data)

    # * we can check the importance of safe paramter in the API below where we are sending Queryset results which is list of dict
    # to the API


# Serialization and Json conversion of QuerySet
def student_list(request):
    stu = Student.objects.all()
    # print(type(stu))
    serializer = StudentSerializer(stu, many=True)
    print(type(serializer.data))


    # jsonData = JSONRenderer().render(serializer.data)
    # return HttpResponse(jsonData)

    # Safe is set to False because if it is True then It will  allow list of dicts to pass 
    # but it is set to true, it will only allow dicts to return 
    return JsonResponse(serializer.data, safe=False)
