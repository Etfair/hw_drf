from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from course.models import Payment, Lesson, Course
from course.seriallizers.course import CourseSerializer
from course.seriallizers.lesson import LessonSerializer
from course.service import get_payment_retrieve
from users.models import User
from users.serializers import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    lesson = SlugRelatedField(slug_field="title", queryset=Lesson.objects.all())
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all(),
                            allow_null=True, required=False)
    lesson = SlugRelatedField(slug_field="title", queryset=Lesson.objects.all(),
                              allow_null=True, required=False)
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all(),
                              allow_null=True, required=False)

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    lesson = LessonSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    url_for_pay = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = ('user', 'lesson', 'course', 'amount', 'date', 'url_for_pay')

    def get_url_for_pay(self, instance) -> None | str | dict:
        if instance.is_paid:
            return None

        session = get_payment_retrieve(instance.session)
        if session.payment_status == 'unpaid' and session.status == 'open':
            return session.url
        elif session.payment_status == 'paid' and session.status == 'complete':
            return None
        status = {
            'session': 'Срок действия сессии истек. Создайте новый платеж.'
        }

        return status
