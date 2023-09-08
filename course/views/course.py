from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from course.paginators import ListPaginator
from course.permissions import IsModerator, IsOwnerOrStaff
from course.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = ListPaginator
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwnerOrStaff | IsModerator]
