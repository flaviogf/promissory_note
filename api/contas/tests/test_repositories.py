from django.test import TestCase

from api.contas.repositories import DjangoContaRepository
from api.contas.tests import ContaModelFactory
from domain.entities import Conta


class DjangoContaRepositoryTests(TestCase):
    def setUp(self):
        self.conta1 = ContaModelFactory.create()
        self.conta2 = ContaModelFactory.create()
        self.sut = DjangoContaRepository()

    def test_lista_por_id(self):
        contas = self.sut.lista_por_id([
            self.conta1.id,
            self.conta2.id
        ])
        contas = list(contas)
        self.assertEqual(2, len(contas))

        for it in contas:
            with self.subTest():
                self.assertIsInstance(it, Conta)
