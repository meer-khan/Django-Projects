# from .views import *
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


# Create Router Object
router = DefaultRouter()
readonly_router = DefaultRouter()

# Register StudentViewSet with Router
router.register("studentapi", views.StudentViewSet, basename = 'student')
readonly_router.register("studentreadonly", views.StudentReadOnlyModelViewSet, basename="hmm")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(readonly_router.urls))

]