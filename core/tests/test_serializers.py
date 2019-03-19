from django.test import TestCase

from core.serializers import PromisoriaSerializer
from core.tests import ContaFactory, ContatoFactory, EnderecoFactory


class PromisoriaSerializerTests(TestCase):
    def setUp(self):
        self.contato1 = ContatoFactory.create()
        self.endereco1 = EnderecoFactory.create()
        self.conta1 = ContaFactory.create()
        self.data1 = {
            'contato': self.contato1.id,
            'endereco': self.endereco1.id,
            'contas': [
                self.conta1.id,
            ]
        }

    def test_promisoria_serializer_is_valid(self):
        self.sut = PromisoriaSerializer(data=self.data1)
        self.assertTrue(self.sut.is_valid())
