from django.urls import path 
from . import views

urlpatterns = [
    path("app2Hello", views.app2_func)
]