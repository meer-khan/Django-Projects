# from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    # *Function Based APIs
    # path("ApiViewCRUD/", view = views.student_api),
    # path("ApiViewCRUD/<int:id>", view = views.student_api),

    # *Testing Class based views: 
    path("ApiViewCRUD/", view = views.StudentAPI.as_view()),
    path("ApiViewCRUD/<int:id>", views.StudentAPI.as_view()),


    


]