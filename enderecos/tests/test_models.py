from django.test import TestCase
from faker import Faker

from enderecos.models import Endereco

fake = Faker('pt_BR')


class EnderecoTests(TestCase):
    def setUp(self):
        self.cep1 = fake.postcode()
        self.rua1 = fake.street_name()
        self.bairro1 = fake.bairro()
        self.numero1 = fake.building_number()

        self.sut = Endereco.objects.create(
            cep=self.cep1,
            rua=self.rua1,
            bairro=self.bairro1,
            numero=self.numero1)

    def test_endereco_create(self):
        self.assertIsInstance(self.sut, Endereco)
        self.assertEqual(self.cep1, self.sut.cep)
        self.assertEqual(self.rua1, self.sut.rua)
        self.assertEqual(self.bairro1, self.sut.bairro)
        self.assertEqual(self.numero1, self.sut.numero)

    def test_endereco_str_(self):
        esperado = f'{self.rua1} - {self.numero1} - {self.bairro1}'
        self.assertEqual(esperado, self.sut.__str__())
