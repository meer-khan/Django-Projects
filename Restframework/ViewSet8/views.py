from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
      stu = Student.objects.all()
      serializer = StudentSerializer(stu,many=True)
      return Response(serializer.data)
    
    def retrieve(self,request, pk=None):
      if pk is not None: 
         
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
      

    def create(self,request):
      serializer = StudentSerializer(data = request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

      return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
      # id = pk 
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance = stu, data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"msg":"Record Updated"},status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
      
    def partial_update(self,request,pk):
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance = stu, 
                                       data = request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response({"msg":"Record Updated"},status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
      

    def destroy(self,request,pk):
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({"msg":"Record Updated"},status=status.HTTP_204_NO_CONTENT)
      return Response({"error":"No Record Found"},status= status.HTTP_400_BAD_REQUEST)
