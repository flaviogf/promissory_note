from django.test import TestCase
from faker import Faker

from enderecos.serializers import EnderecoSerializer

fake = Faker('pt_BR')


class EnderecoSerializerTests(TestCase):
    def setUp(self):
        self.cep1 = fake.postcode()
        self.rua1 = fake.street_name()
        self.bairro1 = fake.bairro()
        self.numero1 = fake.building_number()
        self.data1 = {
            'cep': self.cep1,
            'rua': self.rua1,
            'bairro': self.bairro1,
            'numero': self.numero1
        }

        self.sut = EnderecoSerializer(data=self.data1)

    def test_endereco_serializer_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
