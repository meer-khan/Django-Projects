from django.urls import path, include
from . import views
urlpatterns = [
    path("stu/create/", views.student_create )

]