from django.shortcuts import render
from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



# * To make it a browseable api we need to do some changes, 
# we need to give a parameter of id into the function 
# add another url where url can accept an integer as id 
# change code, and donot get id through request.data.get("id") function but directly from the function parameter
# We need  to add PATCH and PUT functions seperately

@api_view(["GET","POST","PUT","DELETE"])
def student_api(request,id=None):
    if request.method == "GET":
        # id = request.data.get("id",None)
        id = id
        if id is not None: 
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST": 
            serializer = StudentSerializer(data = request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({'msg':"Record Created Successfully"})
            return Response(serializer.errors)
    
    elif request.method == "PUT":
        # id = request.data.get("id")

        id = id
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=stu,data = request.data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Record Updated Successfully"})
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        id = request.data.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':"Record deleted"})
