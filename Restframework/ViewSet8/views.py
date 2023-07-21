from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
      # Attributes given by viewsets
      print("************LIST**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)

      stu = Student.objects.all()
      serializer = StudentSerializer(stu,many=True)
      return Response(serializer.data)
    
    def retrieve(self,request, pk=None):


      # Attributes given by viewsets
      print("************RETRIEVE**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("REQUEST: ", self.request)
      print("FORMAT KWARGS: ", self.format_kwarg)
      print("KWARG: ", self.kwargs)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)

      if pk is not None: 
         
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
      

    def create(self,request):
            # Attributes given by viewsets
      print("************CREATE**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)


      serializer = StudentSerializer(data = request.data)
      if serializer.is_valid():
        print(serializer.validated_data)
        # name = serializer.validated_data['name']
    
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

      return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
            # Attributes given by viewsets
      print("************UPDATE**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)


      # id = pk 
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance = stu, data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response({"msg":"Record Updated"},status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
      
    def partial_update(self,request,pk):
            # Attributes given by viewsets
      print("************PARTIAL UPDATE**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(instance = stu, 
                                       data = request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response({"msg":"Record Updated"},status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
      

    def destroy(self,request,pk):
            # Attributes given by viewsets
      print("************DESTROY**************")
      print("Basename: ", self.basename)
      print("Action: ", self.action)
      print("Detail: ", self.detail)
      print("Suffix: ", self.suffix)
      print("Name: ", self.name)
      print("Description: ", self.description)
      if pk is not None:
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({"msg":"Record Updated"},status=status.HTTP_204_NO_CONTENT)
      return Response({"error":"No Record Found"},status= status.HTTP_400_BAD_REQUEST)
