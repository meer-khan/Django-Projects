# Create your views here.

from rest_framework import generics
from .models import Items
from .serializers import ItemsSerializer

class ItemDetailAPIView(generics.RetrieveAPIView):
    querySet = models.Items.objects.all()
    serializer_class = ItemsSerializer(querySet)


product_detail_view = ItemDetailAPIView.as_view()