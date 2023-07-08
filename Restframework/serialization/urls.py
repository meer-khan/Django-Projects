# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    # URL 1 -- POSTMAN
    path("studentinfo/",view=views.student_detail),

    # URL 2 -- POSTMAN
    path("studentlist/",view=views.student_list)

]