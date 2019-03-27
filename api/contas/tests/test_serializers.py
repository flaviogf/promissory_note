from django.test import TestCase

from api.contas.serializers import ContaSerializer
from api.contas.tests import fake


class ContaSerializerTests(TestCase):
    def setUp(self):
        self.descricao = fake.sentence()
        self.valor = 1000.00
        self.data = {
            'descricao': self.descricao,
            'valor': self.valor
        }
        self.sut = ContaSerializer(data=self.data)

    def test_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
