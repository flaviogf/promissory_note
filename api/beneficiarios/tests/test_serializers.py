from django.test import TestCase

from api.beneficiarios.serializers import BeneficiarioSerializer


class BeneficiarioSerializerTests(TestCase):
    def setUp(self):
        self.nome = 'peter'
        self.documento = '456'
        self.email = 'aranha-humana@marvel.com'
        self.data = {
            'nome': self.nome,
            'documento': self.documento,
            'email': self.email,
        }
        self.sut = BeneficiarioSerializer(data=self.data)

    def test_is_valid(self):
        self.assertTrue(self.sut.is_valid())
