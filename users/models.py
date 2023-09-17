from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.TextField(verbose_name='страна', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Subscription(models.Model):

    course_name = models.CharField(max_length=300, verbose_name='название подписки', **NULLABLE)
    course = models.ForeignKey('course.Course', verbose_name='курс для подписки', on_delete=models.CASCADE, related_name='subscriptions')
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, related_name='subscriptions')
    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка оформлена')

    def __str__(self):
        return f'{self.course} {self.user}'

    class Meta:
        verbose_name = 'Подписка на курс'
        verbose_name_plural = 'Подписки на курс'
