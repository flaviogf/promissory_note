from http import HTTPStatus

from django.test import Client, TestCase


class TestListaContatoView(TestCase):
    def test_lista_contato_view_get(self):
        url = '/contatos/'

        client = Client()

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)
