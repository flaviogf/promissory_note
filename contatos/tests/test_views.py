from http import HTTPStatus

from django.test import Client, TestCase


class TestListaContatoView(TestCase):
    def test_lista_contato_view_get(self):
        url = '/contatos/'

        client = Client()

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)


class TestCadastroContatoView(TestCase):
    def test_cadastra_contato_view_get(self):
        url = '/contatos/criar/'

        client = Client()

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_cadastra_contato_view_post(self):
        request = {
            'nome': 'flavio',
            'email': 'flavio@email.com',
            'telefone': '016999999999',
            'cep': '144000000',
            'rua': 'rua',
            'bairro': 'bairro',
            'numero': '12345'
        }

        url = '/contatos/criar/'

        client = Client()

        response = client.post(url, request)

        self.assertEqual(HTTPStatus.FOUND, response.status_code)
