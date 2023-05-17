from django.db import models

# Create your models here...
class Student(models.Model):
    student_name= models.CharField(max_length=50)
    student_address = models.CharField(max_length=225)

# Adding the __str__ function will replace the queryobject in the django admin panel into the value that we use in the return statment
# Keep in mind that if we are returning the integer value than we need to convert it into string by using str() otherwise
# django will display an error when we click on the id(record) in django admin panel 


    # def __str__(self) -> str:
    #     return self.student_name
    
    # def __str__(self) -> str:
    #     return self.id

    def __str__(self) -> str:
        return str(self.id)
    
    # we can also use f string formatting to concate two or more values in the admin panel using __str__ method 
    def __str__(self): 
        return f"ID is {self.id} {self.student_name} and {self.student_address}"