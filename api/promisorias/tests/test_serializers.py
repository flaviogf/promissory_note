from django.test import TestCase

from api.beneficiarios.tests import BeneficiarioModelFactory
from api.contas.tests import ContaModelFactory
from api.emitentes.tests import EmitenteModelFactory
from api.promisorias.serializers import PromisoriaSerializer


class PromisoriaSerializerTests(TestCase):
    def setUp(self):
        self.beneficiario = BeneficiarioModelFactory.create()
        self.emitente = EmitenteModelFactory.create()
        self.contas = ContaModelFactory.create_batch(5)
        self.data = {
            'emitente': self.emitente.id,
            'beneficiario': self.beneficiario.id,
            'contas': [it.id for it in self.contas]
        }
        self.sut = PromisoriaSerializer(data=self.data)

    def test_is_valid_true(self):
        self.assertTrue(self.sut.is_valid())
