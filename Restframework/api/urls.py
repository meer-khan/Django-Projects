from .views import student_detail
from django.urls import path, include

urlpatterns = [
    path("studentinfo/",view=student_detail)
]