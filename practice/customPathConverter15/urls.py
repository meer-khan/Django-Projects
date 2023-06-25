# from django.contrib import admin
# from django.urls import path, include
# from . import views




from django.contrib import admin
from django.urls import path, register_converter
from . import views , converters

register_converter(converter=converters.FourYearDigitConverter, type_name='yyyy')


urlpatterns = [
    path("cdurl/", views.customDynamicURL ),
    # path('/', views.show_details, name ="subdetails")
    path('session/<yyyy:year>/', views.show_details, name ="detail")

]

# urlpatterns = [
#     # path converter is not set (no data type attached), so "id" is considered as string
#     path('cdurl/', include(views.customDynamicURL))
# ] 