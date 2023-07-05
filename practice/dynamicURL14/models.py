# from django.db import models

# # Create your models here.
# class User(models.Model):
#     # if we give argument blank = True, then field will not longer be required in the form, and 
#     # required argument of field in forms.py will automatically be set to false
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=255)

#     # Setting Name of Model (Table)
#     # 1 - we can create a db_table attribute in models.Model inherited class
#     # 2 - Create a Meta class and than create db_table 

#     # Let's rename Table with first approach 
#     # db_table = "user_registration"
#     # ! First approach does not work, Bard is SHITTTTT!!!!!

#     class Meta:
#         db_table = "user_registration2"