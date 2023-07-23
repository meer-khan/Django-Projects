from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# Model View set provides 6 apis, 
# List, Retrieve, Create, Update, Partial Update, Delete
# Just by writing 2 lines of code and define the router we can utilize the complete CRUD
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  # non Staff users cannot access the admin panel 
  # BasicAuthentication class is used to authenticate the user using email/username and password
  # IsAuthenticated is used to give access to any type of user, either it's a staff, nonstaff, normal user or super user. 