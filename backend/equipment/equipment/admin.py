from django.contrib import admin
from equipment import models


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipment_type', 'serial_number')

class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sn_mask')


admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.EquipmentType, EquipmentTypeAdmin)