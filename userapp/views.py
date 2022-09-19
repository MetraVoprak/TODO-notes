from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer, AppUserModelSerializer, AppUserModelSerializerFull
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import mixins, viewsets



class AppUserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    serializer_class = AppUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = AppUserLimitOffsetPagination
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return AppUserModelSerializer

        return AppUserModelSerializerFull