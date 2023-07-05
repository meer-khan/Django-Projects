from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('addnshow/', views.add_show, name='addnshow')
]
