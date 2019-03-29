"""modulo de testes das models do app promisorias"""
from django.test import TestCase

from api.beneficiarios.tests import BeneficiarioModelFactory
from api.contas.tests import ContaModelFactory
from api.emitentes.tests import EmitenteModelFactory
from api.promisorias.models import PromisoriaModel
from api.promisorias.tests import fake


class PromisoriaModelTest(TestCase):
    """classe responsavel pelos testes da classe PromisoriaModel"""
    def setUp(self):
        self.emitente = EmitenteModelFactory.create()
        self.beneficiario = BeneficiarioModelFactory.create()
        self.contas = ContaModelFactory.create_batch(5)
        self.sut = PromisoriaModel.objects.create(emitente=self.emitente,
                                                  beneficiario=self.beneficiario)
        self.sut.contas.set(self.contas)

    def test_create(self):
        """testa o metodo create"""
        self.assertEqual(self.emitente.id, self.sut.emitente.id)
        self.assertEqual(self.beneficiario.id, self.sut.beneficiario.id)
        self.assertEqual(5, self.sut.contas.count())
