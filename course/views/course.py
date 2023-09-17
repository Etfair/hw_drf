from rest_framework import viewsets
from rest_framework.views import APIView

from course.models import Course
from course.paginators import ListPaginator
from course.seriallizers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = ListPaginator
    serializer_class = CourseSerializer
