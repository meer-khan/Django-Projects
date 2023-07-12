from django.shortcuts import render
from serialization.models import Student

from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views import View

import json
from django.views.decorators.csrf import csrf_exempt
# To apply decorator on Django Class View, we need following class
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):

    def get(self, request, *args, **kwargs): 
        # jsonData = request.data
        try:
            jsonData = json.loads(request.body)
            id = jsonData.get("id")
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)

                return JsonResponse(serializer.data, safe=False)
        except:
        
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data, safe=False)
        
    def post(self,request,*args, **kwargs):
        jsonData = json.loads(request.body)
        serializer = StudentSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':"Record Added successfully"})
        
        return JsonResponse(serializer.errors)

    def put(self,request,*args, **kwargs):
        try:
            jsonData = json.loads(request.body)
            id = jsonData.get("id")
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data = jsonData,partial = True)
            if serializer.is_valid(): 
                serializer.save()
                return JsonResponse({'msg':"record Updated"})
        
            return JsonResponse(serializer.errors)
        except Exception as e:
            return JsonResponse({'msg':"An Error Occurred", 'error': str(e)}, status= 500)

    
    def delete(self,request,*args, **kwargs):
        try:
            jsonData = json.loads(request.body)
            id = jsonData.get("id")
            stu = Student.objects.get(pk=id)
            stu.delete()
            return JsonResponse({'msg': 'Record deleted successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'msg': 'Record not found'}, status=404)
        except Exception as e:
            return JsonResponse({'msg': 'An error occurred', 'error': str(e)}, status=500)


