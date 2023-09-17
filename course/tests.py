from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='course test',
            description='course test'
        )

        self.lesson = Lesson.objects.create(
            title='lesson test',
            description='lesson test',
            course=self.course,
            owner=self.user
        )

        self.lesson_data = {
            'title': 'test 2',
            'description': 'test 2',
            'link': 'youtube.com'
        }

    def test_lesson_list(self):
        """ Тест получения списка уроков"""

        response = self.client.get(
            reverse('lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'title': 'lesson test',
                        'preview': None,
                        'description': 'lesson test',
                        'link': None,
                        'course': self.course.pk,
                        'owner': self.user.pk
                    }
                 ]
             }
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_create_lesson(self):
        """ Тест создания уроков"""
        data = {
            'title': 'test create test',
            'description': 'test test test',
        }
        response = self.client.post(
            '/lesson/create/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_retrieve(self) -> None:
        """ Тест просмотра урока """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/lesson/{self.lesson.pk}/')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_update(self):
        """ Тест обновления урока """
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'update lesson',
            'description': 'update lesson',
        }

        response = self.client.put(
            path=f'/lesson/{self.lesson.pk}/update/',
            data=data,
        )

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/{self.lesson.pk}/delete/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Lesson.objects.all().exists(),
        )

    def tearDown(self) -> None:
        self.user.delete()
        self.course.delete()
        self.lesson.delete()


class ValodatorsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
        )
        self.user.set_password('test')
        self.user.save()

        self.course = Course.objects.create(
            title='course 3',
            description='course 3'
        )

        self.lesson = Lesson.objects.create(
            title='lesson 3',
            description='lesson 3',
            course=self.course,
            owner=self.user
        )

    def test_lesson_validator_create(self):
        data = {
            'title': 'test create test',
            'description': 'test test test',
            'link': 'sky@pro.ru'
        }
        response = self.client.post(
            reverse('lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_course_validator_create(self):
        data = {
            "title": "Test 4",
            "description": "Test 4",
        }

        response = self.client.post(
            '/course/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class CourseTestCase(APITestCase):

    def setUp(self):
        pass

    def test_list_course(self):

        Course.objects.create(
            title='list test',
            description='list test'
        )

        response = self.client.get(
            '/course/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'title': 'list test', 'preview': None, 'description': 'list test',
                 'lesson_count': 0, 'lessons_set': []}]}
        )
        self.assertTrue(
            Course.objects.all().exists()
        )

    def test_create_course(self):
        data = {
            "title": "Test",
            "description": "Test"
        }

        response = self.client.post(
            '/course/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'title': 'Test', 'preview': None, 'description': 'Test', 'lesson_count': 0, 'lessons_set': []}
        )

        self.assertTrue(
            Course.objects.all().exists()
        )
