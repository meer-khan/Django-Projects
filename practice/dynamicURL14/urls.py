from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("student/<id>", views.dynamicURL, name="details" )
]