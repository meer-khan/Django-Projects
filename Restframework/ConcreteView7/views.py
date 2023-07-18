from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     RetrieveAPIView, UpdateAPIView, 
                                     DestroyAPIView, ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateDestroyAPIView)
# Create your views here.

class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer



class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer






class StudentListCreate(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentRetrieveDestroy(RetrieveDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer







# GROUP CLASSES that will perform all operations: 
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


class StudentListCreate(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer



