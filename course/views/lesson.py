from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from course.models import Lesson
from course.paginators import ListPaginator
from course.permissions import IsOwner, IsModerator, IsOwnerOrStaff
from course.seriallizers.lesson import LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner, IsModerator]


class LessonDeleteAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    pagination_class = ListPaginator
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = ListPaginator
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff | IsModerator]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_set_fields = ['course', 'lesson']
    ordering_fields = ['date']


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff, IsModerator]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
