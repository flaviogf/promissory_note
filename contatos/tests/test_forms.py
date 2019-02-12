from django.test import TestCase

from contatos.forms import ContatoForm, EnderecoForm


class TestContatoForm(TestCase):
    def test_contato_form_is_valid_true(self):
        request = {
            'nome': 'Flavio',
            'email': 'flavio@email.com',
            'telefone': '016999999999'
        }

        form = ContatoForm(request)

        self.assertTrue(form.is_valid())


class TestEnderecoForm(TestCase):
    def test_endereco_form_is_valid_true(self):
        request = {
            'cep': '14400000',
            'rua': 'rua',
            'bairro': 'bairro',
            'numero': '12345'
        }

        form = EnderecoForm(request)

        self.assertTrue(form.is_valid())
