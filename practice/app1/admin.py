from django.contrib import admin
from app1.models import Student
# Register your models here.


# To display the complete data in admin panel we use modeladmin class in django
# Previously we were seeing records seperatly, and when we click on the record we see the details of the record 
# but by using modeladmin class we can see details of all records and we donot need to go into sepecific record to show it's details 
# STEPS: 
# 1. we need to create a class that will be inhereted from admin.ModelAdmin
# 2. give all fields name into "list_display" attribute in the form of tuple or list, that we want to display
# 3. Register ModelAdmin class with the Model class in admin.py

class StudentAdmin(admin.ModelAdmin):
    list_display= ["student_name","student_address"]


admin.site.register(Student,StudentAdmin)
