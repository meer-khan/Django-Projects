from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    roll = models.CharField(max_length=20)

    # This method is used to return a string representation of the object,
    #  which is useful for debugging and displaying the object in the admin interface.
    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.student.age}"
