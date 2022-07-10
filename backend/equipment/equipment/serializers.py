import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from equipment.models import Equipment, EquipmentType


class EquipmentTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EquipmentType
        fields = ['id', 'name', 'sn_mask',]


class EquipmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Equipment
        fields = ['id', 'equipment_type', 'serial_number', 'is_deleted',]
        read_only_fields = ['is_deleted',]

    def validate(self, attrs):
        """Валидация серийного номера,
        на соответствие маске типа оборудования"""
        equipment_type = attrs.get('equipment_type')
        serial_number = attrs.get('serial_number')
        sn_mask_regex = equipment_type._get_regex()
        if not re.fullmatch(sn_mask_regex, serial_number):
            raise ValidationError('Указан неверный серийный номер')
        return super().validate(attrs)