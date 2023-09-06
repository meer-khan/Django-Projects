# from .views import *
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# Create Router Object
router = DefaultRouter()
readonly_router = DefaultRouter()

# Register StudentViewSet with Router
router.register("studentapi", views.StudentViewSet, basename = 'student')

urlpatterns = [
    path("", include(router.urls)),

    # To get a login button on browseable API
    path("auth/", include("rest_framework.urls"))

]
