from django.test import TestCase

from api.emitente.serializers import EmitenteSerializer


class EmitenteSerializerTests(TestCase):
    def setUp(self):
        self.nome = 'Bruce'
        self.documento = '123'
        self.email = 'batman@dc.com.br'
        self.endereco = 'gotham'

        self.data = {
            'nome': self.nome,
            'documento': self.documento,
            'email': self.email,
            'endereco': self.endereco,
        }

        self.sut = EmitenteSerializer(data=self.data)

    def test_is_valid(self):
        self.assertTrue(self.sut.is_valid())
