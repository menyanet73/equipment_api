from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class EquipmentTypeViewset(mixins.ListModelMixin, GenericViewSet):
    pass

class EquipmentViewset(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
