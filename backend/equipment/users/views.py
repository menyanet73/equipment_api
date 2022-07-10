from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from users.models import AuthToken, User
from users.serializers import TokenSerializer, UserSerializer


class UserViewset(CreateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny,]


class TokenCreateView(CreateModelMixin,
                      GenericViewSet):
    queryset = AuthToken.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [AllowAny,]
