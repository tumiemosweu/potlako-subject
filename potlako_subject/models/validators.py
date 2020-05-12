from django.core.exceptions import ValidationError

from edc_base.utils import get_utcnow


def date_not_now(value):
    if value == get_utcnow().date():
        raise ValidationError('Cannot be a today\'s date')
