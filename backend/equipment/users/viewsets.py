from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class UsersViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    pass