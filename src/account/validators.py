from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def participant_code_not_zero(value: str):
    if value == '0000':
        raise ValidationError(_('Participant code cannot be zero'), params={'value': value})