from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=100),
    content = models.TextField(blank=True , null= True),
    price = models.DecimalField(default=99.99 , max_digits=15 , decimal_places=2)
