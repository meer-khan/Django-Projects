from django.shortcuts import render
from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# * STATUS CODES
# HTTP_200_OK
# HTTP_201_CREATED
# HTTP_202_ACCEPTED
# HTTP_203_NON_AUTHORITATIVE_INFORMATION
# HTTP_204_NO_CONTENT
# HTTP_205_RESET_CONTENT
# HTTP_206_PARTIAL_CONTENT
# HTTP_207_MULTI_STATUS
# HTTP_208_ALREADY_REPORTED
# HTTP_226_IM_USED

# * To make it a browseable api we need to do some changes, 
# we need to give a parameter of id into the function 
# add another url where url can accept an integer as id 
# change code, and donot get id through request.data.get("id") function but directly from the function parameter

# *NOT NECESSARY REQUIREMET
# We can add PATCH and PUT functions seperately
# In Path method we will set partial True for serializer and in PUT method we donot

@api_view(["GET","POST","PUT","DELETE"])
def student_api(request,id=None):
    if request.method == "GET":
        try:
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            else:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student with the provided ID does not exist."},
                status=status.HTTP_404_NOT_FOUND,)
    
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
