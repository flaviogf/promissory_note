from django.test import TestCase

from contatos.models import Contato
from contatos.serializers import ContatoSerializer, EnderecoSerializer


class TestContatoSerializer(TestCase):
    def test_contato_serializer_is_valid_true(self):
        request = {
            "nome": "flavio",
            "email": "flavio@email.com",
            "telefone": "016999999999",
        }

        serializer = ContatoSerializer(data=request)

        self.assertTrue(serializer.is_valid())

    def test_contato_serializer_is_valid_false_nome_nao_informado(self):
        request = {"nome": "", "email": "flavio@email.com", "telefone": "016999999999"}

        serializer = ContatoSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_contato_serializer_is_valid_false_email_nao_informado(self):
        request = {"nome": "flavio", "email": "", "telefone": "016999999999"}

        serializer = ContatoSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_contato_serializer_is_valid_false_telefone_nao_informado(self):
        request = {"nome": "flavio", "email": "flavio@email.com", "telefone": ""}

        serializer = ContatoSerializer(data=request)

        self.assertFalse(serializer.is_valid())


class TestEnderecoSerializer(TestCase):
    def test_endereco_serializer_is_valid_true(self):
        contato = Contato.objects.create(
            nome="fernando", email="fernando@email.com", telefone="016999999999"
        )

        request = {
            "cep": "11111111",
            "rua": "rua",
            "bairro": "bairro",
            "numero": "12345",
            "contato": contato.contato_id,
        }

        serializer = EnderecoSerializer(data=request)

        self.assertTrue(serializer.is_valid())

    def test_endereco_serializer_is_valid_fals_cep_nao_informado(self):
        contato = Contato.objects.create(
            nome="fernando", email="fernando@email.com", telefone="016999999999"
        )

        request = {
            "cep": "",
            "rua": "rua",
            "bairro": "bairro",
            "numero": "12345",
            "contato": contato.contato_id,
        }

        serializer = EnderecoSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_endereco_serializer_is_valid_false_rua_nao_informado(self):
        contato = Contato.objects.create(
            nome="fernando", email="fernando@email.com", telefone="016999999999"
        )

        request = {
            "cep": "11111111",
            "rua": "",
            "bairro": "bairro",
            "numero": "12345",
            "contato": contato.contato_id,
        }

        serializer = EnderecoSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_endereco_serializer_is_valid_fals_bairro_nao_informado(self):
        contato = Contato.objects.create(
            nome="fernando", email="fernando@email.com", telefone="016999999999"
        )

        request = {
            "cep": "11111111",
            "rua": "rua",
            "bairro": "",
            "numero": "12345",
            "contato": contato.contato_id,
        }

        serializer = EnderecoSerializer(data=request)

        self.assertFalse(serializer.is_valid())

    def test_endereco_serializer_is_valid_fals_numero_nao_informado(self):
        contato = Contato.objects.create(
            nome="fernando", email="fernando@email.com", telefone="016999999999"
        )

        request = {
            "cep": "11111111",
            "rua": "rua",
            "bairro": "bairro",
            "numero": "",
            "contato": contato.contato_id,
        }

        serializer = EnderecoSerializer(data=request)

        self.assertFalse(serializer.is_valid())
