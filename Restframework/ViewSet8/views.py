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