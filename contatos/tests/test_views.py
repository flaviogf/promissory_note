from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from contatos.models import Contato, Endereco, HistoricoContato, HistoricoEndereco


class TestCadastroContatoView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_cadastra_contato_view_get(self):
        url = '/contatos/criar/'

        client = Client()

        client.login(username='flavio', password='teste123!')

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

        client.login(username='flavio', password='teste123!')

        response = client.post(url, request)

        redirect = reverse('contatos:list')

        self.assertRedirects(response, redirect)
        self.assertEqual(1, Contato.objects.count())
        self.assertEqual(1, HistoricoContato.objects.count())
        self.assertEqual(1, HistoricoEndereco.objects.count())


class TestEditaContatoView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

        self.contato = Contato.objects.create(
            nome='Flavio',
            email='flavio@email.com',
            telefone='12345678911',
            usuario=self.usuario)

        self.endereco = Endereco.objects.create(
            contato=self.contato,
            cep='144000000',
            rua='rua',
            bairro='bairro',
            numero='12345')

    def test_edita_contato_view_get(self):
        url = f'/contatos/{self.contato.contato_id}/edita/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_edita_contato_view_post(self):
        request = {
            'nome': 'flavio',
            'email': 'flavio@email.com',
            'telefone': '016999999999',
            'cep': '144000000',
            'rua': 'rua',
            'bairro': 'bairro',
            'numero': '12345'
        }

        url = f'/contatos/{self.contato.contato_id}/edita/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.post(url, request)

        redirect = reverse('contatos:list')

        self.assertRedirects(response, redirect)
        self.assertEqual(1, Contato.objects.count())
        self.assertEqual(2, HistoricoContato.objects.count())
        self.assertEqual(2, HistoricoEndereco.objects.count())


class TestDeletaContatoView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

        self.contato = Contato.objects.create(
            nome='Flavio',
            email='flavio@email.com',
            telefone='12345678911',
            usuario=self.usuario)

        self.endereco = Endereco.objects.create(
            contato=self.contato,
            cep='144000000',
            rua='rua',
            bairro='bairro',
            numero='12345')

    def test_deleta_contato_view_get(self):
        url = f'/contatos/{self.contato.contato_id}/deleta/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_deleta_contato_view_post(self):
        request = {
            'nome': 'flavio',
            'email': 'flavio@email.com',
            'telefone': '016999999999',
            'cep': '144000000',
            'rua': 'rua',
            'bairro': 'bairro',
            'numero': '12345'
        }

        url = f'/contatos/{self.contato.contato_id}/deleta/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.post(url, request)

        redirect = reverse('contatos:list')

        self.assertRedirects(response, redirect)


class TestListaContatoView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flavio')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_lista_contato_view_get(self):
        url = '/contatos/'

        client = Client()

        client.login(username='flavio', password='teste123!')

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)
