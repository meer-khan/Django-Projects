# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    path("ApiViewCRUD/", view = views.student_api)

]