# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [

    # path("ConcreteView/", view = views.StudentList.as_view()),
    path("ConcreteView/<int:pk>", view = views.StudentList.as_view()),



]