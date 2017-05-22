from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        try:
            url_validator('http://' + value)
        except ValidationError:
            raise ValidationError('Url invalida')
    return value


def validate_dot_com(value):
    if 'com' not in value:
        raise ValidationError('Url não possui .com')
    return value
