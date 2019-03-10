from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient, APITestCase

from contatos.models import Contato


class TestContatoViewSet(APITestCase):
    def test_contato_view_set_list(self):
        usuario = get_user_model().objects.create(username="flaviogf")
        usuario.set_password("teste123!")
        usuario.save()

        client = APIClient()

        client.force_authenticate(user=usuario)

        url = reverse("contatos:api-v2-list")

        response = client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_contato_view_set_create(self):
        usuario = get_user_model().objects.create(username="flaviogf")
        usuario.set_password("teste123!")
        usuario.save()

        request = {
            "nome": "fernando",
            "email": "fernando@email.com",
            "telefone": "016999999999",
        }

        client = APIClient()

        client.force_authenticate(user=usuario)

        url = reverse("contatos:api-v2-list")

        response = client.post(url, request)

        self.assertEqual(HTTP_201_CREATED, response.status_code)

    def test_contato_view_set_retrieve(self):
        usuario = get_user_model().objects.create(username="flaviogf")
        usuario.set_password("teste123!")
        usuario.save()

        contato = Contato.objects.create(
            usuario=usuario,
            nome="fernando",
            email="fernando@email.com",
            telefone="016999999999",
        )

        client = APIClient()

        client.force_authenticate(user=usuario)

        url = reverse("contatos:api-v2-detail", kwargs={"pk": contato.contato_id})

        response = client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_contato_view_set_delete(self):
        usuario = get_user_model().objects.create(username="flaviogf")
        usuario.set_password("teste123!")
        usuario.save()

        contato = Contato.objects.create(
            usuario=usuario,
            nome="fernando",
            email="fernando@email.com",
            telefone="016999999999",
        )

        client = APIClient()

        client.force_authenticate(user=usuario)

        url = reverse("contatos:api-v2-detail", kwargs={"pk": contato.contato_id})

        response = client.delete(url)

        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)
