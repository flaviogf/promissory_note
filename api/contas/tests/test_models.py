"""modulo de testes das models do app contas"""
import uuid

from django.test import TestCase

from api.contas.models import ContaModel
from api.contas.tests import fake


class ContaModelTests(TestCase):
    """classe responsavel pelos testes da classe ContaModel"""
    def setUp(self):
        self.descricao = fake.sentence()
        self.valor = 1000.00
        self.sut = ContaModel.objects.create(descricao=self.descricao,
                                             valor=self.valor)

    def test_create(self):
        """testa o metodo create"""
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.descricao, self.sut.descricao)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertIsNone(self.sut.data_recebimento)
        self.assertFalse(self.sut.recebida)
