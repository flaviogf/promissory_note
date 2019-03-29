"""modulo de testes dos serializers do app emitentes"""
from django.test import TestCase

from api.emitentes.serializers import EmitenteSerializer
from api.emitentes.tests import EmitenteModelFactory, fake


class EmitenteSerializerTests(TestCase):
    """classe responsavel pelos testes da classe EmitenteSerializer"""
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.address()
        self.telefone = fake.phone_number()
        self.data = {
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }
        self.sut = EmitenteSerializer(data=self.data)

    def test_is_valid_true(self):
        """testa o metodo is_valid"""
        self.assertTrue(self.sut.is_valid())
