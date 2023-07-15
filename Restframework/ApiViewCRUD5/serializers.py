from rest_framework import serializers
from serialization.models import Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['name','roll','city']












