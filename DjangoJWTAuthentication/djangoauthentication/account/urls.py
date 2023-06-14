from django.contrib import admin
from django.urls import path, include
from account.views import UserRegistrationView
urlpatterns = [

    path("register/",UserRegistrationView.as_view(), name="register" )
]