from django.core.exceptions import ValidationError
from conf.settings import MASK_SYMBOLS

def validate_sn_mask(value):
    if len(value) != 10:
        raise ValidationError('Маска должна содержать 10 символов')
    value_set = set(value)
    for symbol in value_set:
        if symbol not in MASK_SYMBOLS:
            raise ValidationError(f'{symbol} - неподдерживаемый символ')
    return value

