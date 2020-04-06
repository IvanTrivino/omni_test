# Rest Framework imports
from rest_framework.serializers import ModelSerializer

# Models imports
from omni_test.users.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
