from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# Create your views here.


# Model View set provides 6 apis, 
# List, Retrieve, Create, Update, Partial Update, Delete
# Just by writing 2 lines of code and define the router we can utilize the complete CRUD
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  # permission_classes = [IsAuthenticated, AllowAny]
  permission_classes = [IsAdminUser] # this is only accessible by the user who are staff "is staff true"


  # non Staff users cannot access the admin panel 
  # BasicAuthentication class is used to authenticate the user using email/username and password
  # IsAuthenticated is used to give access to any type of user, either it's a staff, nonstaff, normal user or super user. 

  # we can define permission class globally throughout the project by writing following code in settings.py 
#   REST_FRAMEWORK = {
#     'DEFAUL_AUTHENTICATION_CLASSES': [
#      'rest_framework.authentication.BasicAuthentication'
#     ]
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ]
# }

# * IMPORTANT

# if we have set the permissions and authenticaions globally 
# we can override this by adding authenticaion_classes and permission_classes in the api of views.py then global settings will be overridden