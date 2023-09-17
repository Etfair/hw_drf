from django.core.exceptions import ValidationError

have_access = ["null", None, 'youtube.com']


class URLValidator:

    def __call__(self, value):
        if value not in have_access:
            raise ValidationError('Не правильный url')
