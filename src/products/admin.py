from django.contrib import admin
# Register your models here.
# Relative import of the product class
from .models import Product
admin.site.register(Product)
