from django.urls import path

from drf.backend.api.views import ItemDetailAPIView

from . import views

urlPatterns = [
    path("<int:pk>", views.product_detail_view),
    path("<int:pk",views.ItemDetailAPIView.as_view())
]