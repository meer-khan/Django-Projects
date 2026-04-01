from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    roll = models.CharField(max_length=20)

    def __str__(self):
        return self.name