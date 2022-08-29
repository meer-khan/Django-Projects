from django.db import models
# from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Products(models.Model):
    price = models.DecimalField(default=99.99 , max_digits=15 , decimal_places=2),
    title = models.CharField(max_length=120),
    content = models.TextField(blank=True , null= True),
    price = models.DecimalField(default=99.99 , max_digits=15 , decimal_places=2),
    title = models.CharField(max_length=120),
    content = models.TextField(blank=True , null= True),

# class Dummy(models.Model):
#     Name = models.CharField(max_length=255)
#     kgrams = ArrayField(models.CharField(max_length=255))
#     cs = models.DecimalField(max_digits=225, decimal_places=0)
#     hashlist = ArrayField(models.DecimalField(max_digits=225, decimal_places=0))
#     class Meta:
#         db_table = 'Dummy'

