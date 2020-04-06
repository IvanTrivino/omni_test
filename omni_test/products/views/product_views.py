# Rest Framework imports
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Models imports
from omni_test.products.models import Product

# Serializers imports
from omni_test.products.serializers import ProductSerializer


class ListCreateProduct(ListCreateAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def post(self, request):
        data = self.request.data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_status = HTTP_201_CREATED
        else:
            response_data = serializer.errors
            response_status = HTTP_400_BAD_REQUEST

        return Response(response_data, status=response_status)


class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
