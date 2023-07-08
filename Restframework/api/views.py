from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

# Serialization and Json conversion of Model Instance 
def student_detail(request):
    stu = Student.objects.get(id = 1)
    # print(type(stu))
    serializer = StudentSerializer(stu)
    print(type(serializer.data))
    jsonData = JSONRenderer().render(serializer.data)
    print(jsonData)
    print(type(jsonData))
    return HttpResponse(jsonData)


# Serialization and Json conversion of QuerySet
def student_list(request):
    stu = Student.objects.all()
    # print(type(stu))
    serializer = StudentSerializer(stu, many=True)
    print(type(serializer.data))
    jsonData = JSONRenderer().render(serializer.data)
    print(jsonData)
    print(type(jsonData))
    return HttpResponse(jsonData)