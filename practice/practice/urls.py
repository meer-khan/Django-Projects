"""
URL configuration for practice project.

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
from app1 import views as app1
from app2 import views as app2
# OR we can import direct function from the files

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app1.index),
    path("app1/", include("app1.urls")),
    path("app2/", include("app2.urls")),
    path("formloop/", include("looponformandhiddenfields.urls")),
    path("formfield/",include("formfieldarguments.urls")),
    path("postform/",include("postform.urls")),
    path("vf/", include("validatingform.urls")),
    path("redi/", include("redirecting.urls")),
    path('10/',include("formfieldtypes10.urls")),
    path('11/',include("cleaningValidatingFormData11.urls")),
    path('12/',include("stylingFormErrors12.urls")),
    path("13/", include("modelForms13.urls")),
    path("14/", include("dynamicURL14.urls")),
    path("15/", include("customPathConverter15.urls")),


    # path("learnDJ/", app1.my_func),
    # path("myName/", app1.my_func2),
    # path("app2Hello", app2.app2_func)
]
