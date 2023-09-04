from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from course.models import Payment, Lesson, Course
from course.seriallizers.course import CourseSerializer
from course.seriallizers.lesson import LessonSerializer


class PaymentSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=Payment.objects.all())
    lesson = SlugRelatedField(slug_field="title", queryset=Lesson.objects.all())
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'
