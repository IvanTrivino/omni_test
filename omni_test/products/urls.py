# Django imports
from django.urls import path

# Rest Framework imports
from rest_framework.routers import DefaultRouter

# Views imports
from omni_test.products.views import CategoryViewSet, ListCreateProduct, RetrieveUpdateDestroyProduct


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', ListCreateProduct.as_view(), name='list_create_product'),
    path('<int:id>', RetrieveUpdateDestroyProduct.as_view(), name='retrieve_update_destroy_product'),
] + router.urls
