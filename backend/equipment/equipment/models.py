from django.db import models
from equipment.validators import validate_sn_mask
from conf.settings import MASK_SYMBOLS


class EquipmentType(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название оборудования')
    sn_mask = models.CharField(max_length=10,
                               validators=[validate_sn_mask,],
                               verbose_name='Маска серийного номера',
                               help_text='N:0-9, A:A-Z, a:a-z, X:0-Z, Z:-,_,@')

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'

    def _get_regex(self):
        """Преобразует маску в regex строку
        для валидации серийного номера оборудования"""
        regex_string = r''
        for symbol in self.sn_mask:
            regex_string += MASK_SYMBOLS[symbol]
        return regex_string
    
    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):
    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        related_name='equipments',
        verbose_name='Тип оборудования'
    )
    serial_number = models.CharField(max_length=10,
                                     verbose_name='Серийный номер')
    is_deleted = models.BooleanField(default=False,
                                     verbose_name='Метка удаления')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        unique_together=['equipment_type', 'serial_number']