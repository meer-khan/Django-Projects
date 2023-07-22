from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


# Create your views here.


# Model View set provides 6 apis, 
# List, Retrieve, Create, Update, Partial Update, Delete
# Just by writing 2 lines of code and define the router we can utilize the complete CRUD
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer




# ReadOnlyModelViewSet Provides list and retrieve functionalities only
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
      