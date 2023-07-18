# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    # *Generic Mixin Classes

    # * GROUP 1
    # path("GenericAPIandMixin/", view = views.StudentCreate.as_view()),
    # path("GenericAPIandMixin/", view = views.StudentList.as_view()),


    # * GROUP 2
    # StudentRetrieve Function only works on 'pk' parameter
    # path("GenericAPIandMixin/<int:pk>", views.StudentRetrieve.as_view()),
    # path("GenericAPIandMixin/<int:pk>", views.StudentUpdate.as_view()),
    # path("GenericAPIandMixin/<int:pk>", views.StudentDestroy.as_view()),


    # LIST AND CREATE URL 
    # * NEW GROUP 1
    path("GenericAPIandMixin/", view = views.LCStudentAPI.as_view()),

    # * NEW GROUP 2
    path("GenericAPIandMixin/<int:pk>", view = views.RUPStudentAPI.as_view()),


]