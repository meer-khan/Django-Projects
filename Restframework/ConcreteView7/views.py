from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
# Create your views here.

class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer