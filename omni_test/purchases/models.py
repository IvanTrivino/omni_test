# Django imports
from django.db import models

# Models imports
from omni_test.users.models import User
from omni_test.products.models import Product


class Purchase(models.Model):

    client = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    purchase_date = models.DateTimeField(auto_now=True)
    prise = models.CharField(max_length=10)

    class Meta:
        db_table = 'purchases'

    def __str__(self):
        return '{} {} - {}'.format(self.client.first_name, self.client.last_name, self.product.name)
