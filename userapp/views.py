from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
