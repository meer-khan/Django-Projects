# Create your views here.

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Items
from .serializers import ItemsSerializer



class ItemListAPIView(generics.ListAPIView):
    queryset = Items.objects.all()
    print("Length of Query SET")
    print(len(queryset))
    serializer_class = ItemsSerializer


product_list_view = ItemListAPIView.as_view()

class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    print("Length of Query SET")
    print(len(queryset))
    serializer_class = ItemsSerializer
    
    
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
    serializer_class = ItemsSerializer
    
    
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('desc') or None
        print(content)
        if content == None: 
            
            content = title
            print(content)
            serializer.save(desc=content)

# product_create_view = ItemCreateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance.desc)
        if not instance.desc:
            instance.desc = instance.title
            ## 

product_update_view = ProductUpdateAPIView.as_view()



@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Items, pk=pk)
            data = ItemsSerializer(obj, many=False).data
            print(type(data))
            return Response(data)
        # list view
        queryset = Items.objects.all() 
        data = ItemsSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ItemsSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('desc') or None
            if content is None:
                content = title
            serializer.save(desc=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)


