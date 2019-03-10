from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient, APITestCase

from contatos.models import Contato


class TestContaViewSet(APITestCase):
    def test_conta_view_set_list(self):
        usuario = get_user_model().objects.create(username="flaviogf")
        usuario.set_password("teste123!")
        usuario.save()

        client = APIClient()

        client.force_authenticate(user=usuario)

        contato = Contato.objects.create(
            nome="flavio", email="flavio@email.com", telefone="016999999999"
        )

        url = reverse("contas:api-v2-list")

        response = client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)
