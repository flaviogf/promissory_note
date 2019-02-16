from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class TestRegistrarUsuarioView(TestCase):
    def test_registrar_usuario_get(self):
        url = '/usuarios/registrar/'

        client = Client()

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_registrar_usuario_post(self):
        request = {
            'username': 'flaviogf',
            'password1': 'teste123!',
            'password2': 'teste123!',
        }

        url = '/usuarios/registrar/'

        client = Client()

        response = client.post(url, request)

        redirect = reverse('usuarios:login')

        self.assertRedirects(response, redirect)


class TestLoginView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_login_view_get(self):
        url = '/usuarios/login/'

        client = Client()

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_login_view_post(self):
        request = {'username': 'flavio', 'password': 'teste123!'}

        url = '/usuarios/login/'

        client = Client()

        response = client.post(url, request)

        redirect = reverse('contatos:list')

        self.assertRedirects(response, redirect)


class TestLogoutView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_logout_view_post(self):
        url = '/usuarios/logout/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.get(url)

        redirect = reverse('usuarios:login')

        self.assertRedirects(response, redirect)
