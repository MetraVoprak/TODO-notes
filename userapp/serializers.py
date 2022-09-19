from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, Serializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "first_name", "last_name", "email")


class AppUserModelSerializerFull(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')
