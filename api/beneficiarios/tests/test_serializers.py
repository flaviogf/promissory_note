from django.test import TestCase

from api.beneficiarios.serializers import BeneficiarioSerializer
from api.beneficiarios.tests import fake


class BeneficiarioSerializerTests(TestCase):
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.address()
        self.telefone = fake.phone_number()
        self.data = {
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }
        self.sut = BeneficiarioSerializer(data=self.data)

    def test_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
