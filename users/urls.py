from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, UserCreateAPIView, UserListAPIView, SubscriptionCreateAPIView, \
    SubscriptionDestroyAPIView

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='create_user'),
    path('users/', UserListAPIView.as_view(), name='list_user.all'),

    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(),
         name='subscription_delete'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + router.urls
