from equipment.serializers import EquipmentSerializer, EquipmentTypeSerializer
from equipment.models import Equipment, EquipmentType
from equipment.viewsets import EquipmentTypeViewset, EquipmentViewset


class EquipmentView(EquipmentViewset):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        equipment_type = self.request.query_params.get('equipment_type')
        serial_number = self.request.query_params.get('serial_number')
        queryset = Equipment.objects.filter(is_deleted=False)
        if equipment_type:
            queryset = queryset.filter(equipment_type=equipment_type)
        if serial_number:
            queryset = queryset.filter(serial_number=serial_number)
        return queryset


class EquipmentTypeView(EquipmentTypeViewset):
    serializer_class = EquipmentTypeSerializer
    
    def get_queryset(self):
        name = self.request.query_params.get('name')
        sn_mask = self.request.query_params.get('sn_mask')
        queryset = EquipmentType.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        if sn_mask:
            queryset = queryset.filter(sn_mask__icontains=sn_mask)
        return queryset
