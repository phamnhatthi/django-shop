from django.contrib import admin

# Register your models here.
from .models import Product
admin.site.register(Product)  # Register the Product model with the admin site
