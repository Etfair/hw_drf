from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course, Lesson
from course.seriallizers.lesson import LessonDetailSerializer, LessonSerializer
from users.serializers import SubscriptionSerializer


class CourseSerializer(serializers.ModelSerializer):
    # lessons = serializers.SerializerMethodField(read_only=True)
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lessons_set = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['title', 'preview', 'description', 'lesson_count', 'lessons_set']

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson = LessonDetailSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CourseCreateSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        lesson = validated_data.pop('lesson')
        course_item = Course.objects.create(**validated_data)

        for item in lesson:
            Lesson.objects.create(**item, course=course_item)

        return course_item
