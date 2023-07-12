from rest_framework import serializers
from serialization.models import Student




# * If we want to create a custome validator function we can create it outside the class 
# intiate a field outside meta class on which we want to apply this validation function 
# pass this function into validators argument of that field
# Check code line of 18 in this file where we pass custom validator function
def custom_validator(value):
    # Perform custom validation logic
    if value < 0:
        raise serializers.ValidationError("Value must be greater than or equal to zero.")


class StudentSerializer(serializers.ModelSerializer):
    # my_field = serializers.IntegerField(validators=[custom_validator])
    
    # we get create method, update method in Model Serializer that's why people use ModelSerializers
    class Meta: 
        model = Student
        fields = ['name','roll','city']


        # * include all fields
        # fields = '__all__'

        # * exclude one field
        # exclude = ['roll']












