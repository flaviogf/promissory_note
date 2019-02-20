from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from contatos.models import Contato


class ContaCadastroContaContatoView(TestCase):
    def test_cadastro_conta_contato_view_get(self):
        usuario = get_user_model().objects.create(username='flavio')
        usuario.set_password('teste123!')
        usuario.save()

        contato = Contato.objects.create(
            nome='fernando', email='fernando@email.com', telefone='016999999999')

        client = Client()

        response = client.get(f'/contas/contato/{contato.contato_id}/')

        self.assertEqual(HTTPStatus.OK, response.status_code)
