from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Lesson
from users.models import Subscription, User


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='test course',
            description='test course description',
        )

        self.lesson = Lesson.objects.create(
            title='test lesson',
            description='test lesson description',

        )

    def test_subscription_create(self):
        data = {
            'course': self.course.id,
            'user': self.user.id,
        }

        response = self.client.post(
            '/users/subscription/create/',
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_delete(self):
        # self.client.force_authenticate(user=self.user)

        subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
        )

        response = self.client.delete(
            f'/users/subscription/delete/{subscription.pk}/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Subscription.objects.all().exists(),
        )
