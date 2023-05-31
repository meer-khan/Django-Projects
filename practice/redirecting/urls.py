from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("redirecting/", views.redirecting ),
    path("success/", views.success)
]