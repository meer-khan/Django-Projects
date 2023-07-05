from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.add_show, name='addnshow'), 

    path('addnshow/', views.add_show, name='addnshow'), 
    path("delete/<int:id>" , views.delete_data, name="delete"),
    path("<int:id>/" , views.update_data, name="update")

]
