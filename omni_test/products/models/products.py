# Django imports
from django.db import models

# Models imports
from omni_test.products.models import Category


class Product(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)
