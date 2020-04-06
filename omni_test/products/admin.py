# Django imports
from django.contrib import admin

# Models imports
from omni_test.products.models import Product, Category


admin.site.register(Category)
admin.site.register(Product)
