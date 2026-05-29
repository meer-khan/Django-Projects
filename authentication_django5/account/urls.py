from django.urls import path

from .views import register, login_user, profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("profile/", profile, name="profile"),
]