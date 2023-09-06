from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, 
                                        DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly)
from .custompermissions import MyPermission
# Create your views here.


# Model View set provides 6 apis, 
# List, Retrieve, Create, Update, Partial Update, Delete
# Just by writing 2 lines of code and define the router we can utilize the complete CRUD
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  # permission_classes = [IsAuthenticated, AllowAny]
  # permission_classes = [IsAdminUser] # this is only accessible by the user who are staff "is staff true"
  # permission_classes = [IsAuthenticatedOrReadOnly]
  # permission_classes = [DjangoModelPermissions]
  # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

  # This is custome permission
  permission_classes = [MyPermission]














