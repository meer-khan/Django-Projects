from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    print("This is my_discount",my_discount)
    print(type(my_discount))
    class Meta: 
        model = Items
        fields = [
            "title" , 
            "desc" , 
            "price" , 
            "sale_price" , 
            # "get_discount"
            "my_discount"
            ]
# We can access the get_discount method of the Items Model but What if we want to change the name to "my_discount" and  access the 
# get_discount method of the Items
    def get_my_discount(self, obj):
        # print(type(obj))
        try:
            return obj.get_discount()
        except:
            return None