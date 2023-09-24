from datetime import datetime, timedelta
from django.utils import timezone
from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from course.models import Course
from users.models import Subscription, User


@shared_task
def check_update():
    last_check = cache.get('last_check')
    if not last_check:
        cache.set('last_check', timezone.now(), 100)
        last_check = cache.get('last_check')

    update_course = Course.objects.filter(last_update_date__gt=last_check)
    if not update_course:
        cache.set("last_check", timezone.now(), 100)
        return

    subscriptions = Subscription.objects.filter(course__in=update_course).select_related('owner').distinct()
    email_to_send = list(subscriptions.values_list('owner__email', flat=True))
    send_mail(
        subject='Обновление курса',
        message='У курса вышло обновление',
        from_email=EMAIL_HOST_USER,
        recipient_list=email_to_send
    )
    cache.set('last_check', timezone.now(), 100)


@shared_task
def check_last_activity():
    user = User.objects.all()
    if user.is_active and user.last_login < datetime.now() - timedelta(days=30):
        user.is_active = False
        user.save()
