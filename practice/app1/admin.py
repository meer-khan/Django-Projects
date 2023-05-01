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

# _________________________CODE1________________________________
# class StudentAdmin(admin.ModelAdmin):
#     # "id" is not mentioned in the Model class but we can use it becasue django creates id field in DB if we donot 
#     # specify any field as primary key.
#     list_display= ["id","student_name","student_address"]


# admin.site.register(Student,StudentAdmin)
# _________________________END__________________________________

# _________________________CODE2________________________________
# We can also register our ModelAdmin Class with Model Class for admin using Decorator using below Syntax: 
# It will work same as above.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # "id" is not mentioned in the Model class but we can use it becasue django creates id field in DB if we donot 
    # specify any field as primary key.
    list_display= ["id","student_name","student_address"]
# _________________________END__________________________________
