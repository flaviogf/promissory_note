from django.test import TestCase
from faker import Faker

from contas.serializers import ContaSerializer

fake = Faker('pt_BR')


class ContaSerializerTests(TestCase):
    def setUp(self):
        self.descricao1 = fake.sentence()
        self.valor1 = 10000
        self.data1 = {
            'descricao': self.descricao1,
            'valor': self.valor1,
        }
        self.sut = ContaSerializer(data=self.data1)

    def test_conta_serializer_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
