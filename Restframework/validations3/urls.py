# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path("validataion/", view = views.StudentAPI.as_view())

]