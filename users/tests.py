from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            'username': 'user_1',
            'email': 'user1@mail.ru',
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'password1': 'FDSF234Lfasd',
            'password2': 'FDSF234Lfasd',
        }

    def test_form_registration_get(self):
        """Проверка доступности формы регистрации"""
        path = reverse('users:register')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/user_form.html')

    def test_user_registration_success(self):
        """Проверка процесса регистрации"""
        user_model = get_user_model()
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def test_user_registration_password_error(self):
        """Проверка на ввод несовпадающих паролей"""
        self.data['password2'] = '342023adfsAdsff'
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Введенные пароли не совпадают")

    def test_user_registration_user_exists_error(self):
        """Проверка на попытку повторной регистрации"""
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])
        path = reverse('users:register')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Пользователь с таким именем уже существует.")