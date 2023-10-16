from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Lesson, Course
from users.models import User, UserRoles


class EducationTestCase(APITestCase):
    def setUp(self):
        """Заполнение первичных данных"""

        self.user = User.objects.create(
            username='admin@test.com',
            email='admin@test.com',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role=UserRoles.MEMBER,
        )
        self.user.set_password('12345')
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='test title course',
            description='test description course'
        )

        self.lesson = Lesson.objects.create(
            title='test title lesson',
            description='test description lesson',
            course=self.course,
            owner=self.user
        )





    def test_getting_lesson_list(self):
        """ Тест получения списка уроков """

        response = self.client.get(
            reverse('education:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": 3,
                        "title": 'test title lesson',
                        "description": 'test description lesson',
                        "picture": None,
                        "link": None,
                        "course": 2,
                        "owner": 2

                    }
                ]
            }
        )

    def test_create_lesson(self):
        """ Тест создания урока """

        data = {
            'title': 'test create lesson',
            'description': 'test create description lesson',
            "course": 1

        }

        response = self.client.post(reverse('education:lesson_create'), data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                    "id": 2,
                    "title": 'test create lesson',
                    "description": 'test create description lesson',
                    "picture": None,
                    "link": None,
                    "course": 1,
                    "owner": 1

                    }

        )

        self.assertEqual(
            2,
            Lesson.objects.all().count()
        )

    def test_update_lesson(self):
        """ Тест обновления урока """

        data = {
            'title': 'update test',
        }

        response = self.client.put(
            reverse('education:lesson_update', args=[self.lesson.pk]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.lesson.refresh_from_db()

        self.assertEqual(
            self.lesson.title,
            'update test'
        )

    def test_lesson_delete(self):
        """ Тест удаления урока """

        self.client.delete(
            reverse('education:lesson_delete', args=[self.lesson.pk])
        )

        self.assertFalse(Lesson.objects.filter(id=self.lesson.pk).exists())
