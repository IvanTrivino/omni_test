# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Serilalizers imports
from omni_test.purchases.serializers import PurchaseSerializer


class GeneratePurchaseView(APIView):

    def post(self, request):
        data = self.request.data
        data['client_id'] = self.request.user.id
        serializer = PurchaseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_status = 201
        else:
            response_data = serializer.errors
            response_status = 400

        return Response(response_data, status=response_status)
