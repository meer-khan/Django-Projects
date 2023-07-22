from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
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
      