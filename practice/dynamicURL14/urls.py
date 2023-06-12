from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path converter is not set (no data type attached), so "id" is considered as string
    path("student/<id>", views.dynamicURL, name="detail" ),
    path("home/", views.home, name = "home"),
    path("", views.home, name = "home"),
    path("details/<int:id>", views.integerID, name = "userDetails"),
    path("details/<int:id>/<int:subid>", views.integerID, name = "subDetails"),



]