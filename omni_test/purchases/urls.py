# Django imports
from django.urls import path

# Views imports
from omni_test.purchases.views import GeneratePurchaseView


urlpatterns = [
    path('generate/', GeneratePurchaseView.as_view(), name='generate_purchase'),
]
