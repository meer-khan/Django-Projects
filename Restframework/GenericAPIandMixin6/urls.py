# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    # *Generic Mixin Classes
    path("GenericAPIandMixin/", view = views.StudentCreate.as_view()),
    # path("GenericAPIandMixin/", view = views.StudentList.as_view()),

    # path("GenericAPIandMixin/<int:id>", views.StudentAPI.as_view()),


    


]