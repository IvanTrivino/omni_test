# Rest Framework imports
from rest_framework.serializers import ModelSerializer, IntegerField

# Models imports
from omni_test.products.models import Product

# Serializers imports
from omni_test.products.serializers import CategorySerializer


class ProductSerializer(ModelSerializer):

    category_id = IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
