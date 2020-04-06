# Rest Framework Imports
from rest_framework.viewsets import ModelViewSet

# Models imports
from omni_test.products.models import Category

# Serializers imports
from omni_test.products.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
