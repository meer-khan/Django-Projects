"""
URL configuration for Restframework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("serialization.urls")),
    path("api/deserialization/", include("deserialization.urls")),
    path("api3/",include("validations3.urls")),
    path("api4/", include("ModelSerializer4.urls")),
    path("api5/", include("ApiViewCRUD5.urls")),
    path('api6/',include("GenericAPIandMixin6.urls")),
    path('api7/',include("ConcreteView7.urls")),
    path("api8/", include("ViewSet8.urls")),
    path("api9/", include("ModelViewSet9.urls")),
    path("api10/", include("BasicAuthenticationAndPermissions10.urls")),
    path("api11/", include("SessionAuthentication11.urls")),
    path("api12/", include("CustomPermission12.urls")),
    path("api13/", include("JWTAuthentication13.urls"))

    


]
