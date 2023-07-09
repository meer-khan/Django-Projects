from rest_framework import serializers
from serialization.models import Student

# class StudentSerializer(serializers.Serializer):
#     print("INTO SERIALIZER")
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)



class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    # def create(self, validate_data):
    #     print("INTO CREATE FUNCTION")
    #     return Student.objects.create(**validate_data)