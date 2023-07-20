# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [

    path("ViewSet8/", view = views.StudentList.as_view()),
    path("ViewSet8/<int:pk>", view = views.StudentList.as_view()),



]