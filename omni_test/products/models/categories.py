# Django imports
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)
