# Create your views here.

from rest_framework import generics
from .models import Items
from .serializers import ItemsSerializer



class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    print("Length of Query SET")
    print(len(queryset))
    serializer_classes = ItemsSerializer
    
    
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('desc') or None
        print(content)
        if content == None: 
            
            content = title
            print(content)
            serializer.save(desc=content)

# change this variable to product_create_list_view and update the URL as well
product_create_view = ItemListCreateAPIView.as_view()

class ItemDetailAPIView(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


product_detail_view = ItemDetailAPIView.as_view()


class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Items.objects.all()
    print("Length of Query SET")
    print(len(queryset))
    serializer_classes = ItemsSerializer
    
    
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('desc') or None
        print(content)
        if content == None: 
            
            content = title
            print(content)
            serializer.save(desc=content)

product_create_view = ItemCreateAPIView.as_view()


