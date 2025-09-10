from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer  # Замените your_app на имя вашего приложения


class RegistrViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('registration')  # Укажите имя вашего URL-маршрута
        self.valid_payload = {
            'username': 'maximych',
            'email': 'test@example.com',
            'password': 'testpassword123',
            # Добавьте другие обязательные поля для UserSerializer
        }
        self.invalid_payload = {
            'username': '',  # Пустое обязательное поле
            'email': 'invalid-email',  # Неправильный формат email
            'password': 'short',  # Слишком короткий пароль
        }

    def test_registration_with_valid_data(self):
        """Тест успешной регистрации с валидными данными"""
        response = self.client.post(
            self.url,
            data=self.valid_payload,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
