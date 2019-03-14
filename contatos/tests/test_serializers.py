from django.test import TestCase
from faker import Faker

from contatos.serializers import ContatoSerializer

fake = Faker('pt_BR')


class ContatoSerializerTests(TestCase):
    def setUp(self):
        self.nome1 = fake.name()
        self.email1 = fake.email()
        self.telefone1 = fake.phone_number()
        self.data1 = {
            'nome': self.nome1,
            'email': self.email1,
            'telefone': self.telefone1
        }

        self.sut = ContatoSerializer(data=self.data1)

    def test_contato_serializer_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
