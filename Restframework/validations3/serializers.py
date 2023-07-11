from rest_framework import serializers
from serialization.models import Student


def city_validation(data):
    if data == 'MBDIN':
        raise serializers.ValidationError("no city available")
    return data
class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, validators = [city_validation])

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)

        instance.save()
        return instance



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

