from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_create_view),
    path("<int:pk>/", views.product_detail_view),
    # path("<int:pk",views.ItemDetailAPIView.as_view())
    
]