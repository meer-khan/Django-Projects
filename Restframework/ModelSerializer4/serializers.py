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


    # Let's start to perform some validations
    # We want to make a field read only- which means it cannot be updated 
    # We can do it like below 
    # but what if we want to make more field read_only, you can refer to line 31 and 32 for second method

    # *READ ONLY METHOD 1
    name = serializers.CharField(read_only=True)
    class Meta: 
        model = Student
        fields = ['name','roll','city']

        # *READ ONLY METHOD 2
        # read_only_fields = ['name','city']

        # *READ ONLY METHOD 3
        # we can provide multiple fields, like write_only, required, etc.
        # extra_kwargs = {'name':{'read_only',True, }}


        # * include all fields
        # fields = '__all__'

        # * exclude one field
        # exclude = ['roll']


# * We can implement Field Level and Object Level validations in ModelSerializer same as serializer
        # FIRST DJNAGO WILL EXECUTE FIELD LEVEL VALIDATORS AND THEN OBJECT LEVEL VALIDATIONS


    # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value
    

    # Object Level Validation
    def validate(self,data):
        name = data.get('name')
        city = data.get('city')
        if data.get('roll') == 200:
            raise serializers.ValidationError("Ohh bhai kia kar raha hai tu?")
        if name.lower() == "kashif" and city != "MBDIN":
            raise serializers.ValidationError(f"Ohoo {name} should be from MBDIN")
        
        return data











