from django.conf import settings
from django.db import models

import users
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    preview = models.ImageField(upload_to='course/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    preview = models.ImageField(upload_to='course/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, default=None, verbose_name='курс')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    Cash = 'Cash'
    money_transfer = 'money_transfer'

    PAYMENT_METHOD_CHOICES = [
        (Cash, 'Наличные'),
        (money_transfer, 'Перевод'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')

    amount = models.IntegerField(verbose_name='сумма оплаты')
    method = models.CharField(max_length=14, choices=PAYMENT_METHOD_CHOICES, **NULLABLE, verbose_name='способ оплаты')
    date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')

    def __str__(self):
        return f'{self.amount}({self.method}) - {self.date}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-course', '-lesson', '-date', '-method')
