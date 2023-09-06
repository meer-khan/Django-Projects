# from .views import *
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Create Router Object
router = DefaultRouter()
readonly_router = DefaultRouter()

# Register StudentViewSet with Router
router.register("studentapi", views.StudentViewSet, basename = 'student')

urlpatterns = [
    path("", include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name = 'token_verify'),


    # To get a login button on browseable API
    path("auth/", include("rest_framework.urls"))

]
