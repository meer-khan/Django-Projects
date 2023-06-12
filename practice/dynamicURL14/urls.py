from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path converter is not set (no data type attached), so "id" is considered as string
    path("student/<id>", views.dynamicURL, name="details" )
]