from serialization.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
# Create your views here.

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
