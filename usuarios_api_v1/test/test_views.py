from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase

from usuarios_api_v1.views import UsuarioViewSet


class TestUsuarioViewSet(APITestCase):
    def test_usuario_view_set_created(self):
        url = reverse('usuarios_api_v1:create')

        request = {
            'username': 'flavio',
            'password1': 'teste123!',
            'password2': 'teste123!'
        }

        response = self.client.post(url, request)

        self.assertEqual(HTTP_201_CREATED, response.status_code)
