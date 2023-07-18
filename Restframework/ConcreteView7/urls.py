# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [

    # * NEW GROUP 1
    path("ConcreteView/", view = views.LCStudentAPI.as_view()),


]