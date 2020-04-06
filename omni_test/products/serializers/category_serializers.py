# Rest Framework imports
from rest_framework.serializers import ModelSerializer

# Models imports
from omni_test.products.models import Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
