from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from contatos.models import Contato


class TestContasContatoView(TestCase):
    def test_cadastro_conta_contato_view_get(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        contato = Contato.objects.create(usuario=usuario,
                                         nome='fernando', email='fernando@email.com', telefone='016999999999')

        client = Client()

        client.login(username='flavio', password='teste123!')

        url = reverse('contas:contato-create',
                      kwargs={'contato_id': contato.contato_id})

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)
