# from django.contrib import admin
# from django.urls import path, include
# from . import views




from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("cdurl/", views.customDynamicURL )
]

# urlpatterns = [
#     # path converter is not set (no data type attached), so "id" is considered as string
#     path('cdurl/', include(views.customDynamicURL))
# ] 