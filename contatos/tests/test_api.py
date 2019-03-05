from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from contatos.models import Contato


class TestContatoAPIView(APITestCase):
    def test_get(self):
        usuario = get_user_model().objects.create(username='flaviogf')
        usuario.set_password('teste123!')
        usuario.save()

        contato = Contato.objects.create(usuario=usuario,
                                         nome='fernando',
                                         email='fernando@email.com',
                                         telefone='016999999999')

        client = APIClient()

        client.force_authenticate(user=usuario)

        url = reverse('contatos:contatos_api_v1',
                      kwargs={'contato_id': contato.contato_id})

        response = client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)
