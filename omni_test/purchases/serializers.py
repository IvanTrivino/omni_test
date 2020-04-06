# Rest Framework imports
from rest_framework.serializers import ModelSerializer, IntegerField

# Models imports
from omni_test.purchases.models import Purchase

# Serializers imports
from omni_test.users.serializers import UserSerializer
from omni_test.products.serializers import ProductSerializer


class PurchaseSerializer(ModelSerializer):

    client_id = IntegerField(write_only=True)
    product_id = IntegerField(write_only=True)

    client = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'
