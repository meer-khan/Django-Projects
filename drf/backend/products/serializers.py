from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    print("This is my_discount",my_discount)
    print(type(my_discount))
    class Meta: 
        model = Items
        print("IM in META")
        fields = [
            "title" , 
            "desc" , 
            "price" , 
            "sale_price" , 
            #"get_discount"
            "my_discount"
            ]
# We can access the get_discount method of the Items Model but What if we want to change the name to "my_discount" and  access the 
# get_discount method of the Items
    # print("Get my discout")
    def get_my_discount(self, obj):
        print("THIS IS OBJ",obj)
        return obj.get_discount()
        # print(type(obj))
        # try:
        #     print("Im in Try")
        #     return obj.get_discount()
        # except:
        #     print("Im in Except")
        #     return None