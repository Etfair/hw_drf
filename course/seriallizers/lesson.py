from django.core.validators import URLValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from course.models import Lesson
have_access = ["null", None, 'youtube.com']


class LessonSerializer(serializers.ModelSerializer):
    def validate_link(self, instance):
        print(instance)
        if instance not in have_access:
            raise serializers.ValidationError('Не правильный url')
        return instance

    class Meta:
        model = Lesson
        fields = ('title', 'preview', 'description', 'link', 'course', 'owner')


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
