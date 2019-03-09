from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APITestCase


class UsuarioViewSet(APITestCase):
    def test_usuario_view_set_registra(self):
        url = reverse("usuarios:api-v2-registra")

        request = {
            "username": "flavio",
            "password1": "teste123!",
            "password2": "teste123!",
        }

        response = self.client.post(url, request)

        self.assertEqual(HTTP_201_CREATED, response.status_code)

    def test_usuario_view_set_login(self):
        usuario = get_user_model().objects.create(username="flavio")
        usuario.set_password("teste123!")
        usuario.save()

        url = reverse("usuarios:api-v2-login")

        request = {"username": "flavio", "password": "teste123!"}

        response = self.client.post(url, request)

        self.assertEqual(HTTP_200_OK, response.status_code)
