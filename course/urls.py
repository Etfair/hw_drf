from django.urls import path
from rest_framework import routers

from course.views.course import *
from course.views.lesson import *
from course.views.payment import *

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='create_payment'),
    path('payment/', PaymentListAPIView.as_view(), name='list_payment'),
]

router = routers.SimpleRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns += router.urls
