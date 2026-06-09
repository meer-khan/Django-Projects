from django.contrib import admin
from product.models import Product


class ProductAdminModel(admin.ModelAdmin):
    model = Product
    list_display = ["id", "name", "description", "price", "created_at", "updated_at"]
admin.site.register(Product, ProductAdminModel)
# Register your models here.
