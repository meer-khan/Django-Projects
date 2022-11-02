from email.policy import default
from django.db import models

# Create your models here.




class Dummy(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    kgrams = models.TextField()  # This field type is a guess.# This field type is a guess.

class Items(models.Model):
    # kgrams = models.TextField()  
    title = models.CharField(max_length=100, default=None)
    desc = models.TextField(blank=True, null = True)
    price = models.DecimalField(decimal_places= 2 , default=9.99, max_digits=15)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    
    def get_discount(self):
        return "122"