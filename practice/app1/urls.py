from django.urls import path 
from . import views

urlpatterns = [
    path("learnDJ/", views.my_func),
    path("myName/", views.my_func2),
]