from datetime import date

from django.test import TestCase
from faker import Faker

from contas.models import Conta

fake = Faker()


class ContaTests(TestCase):
    def setUp(self):
        self.descricao1 = fake.sentence()
        self.valor1 = 10000
        self.sut = Conta.objects.create(
            descricao=self.descricao1, valor=self.valor1)

    def test_conta_create(self):
        self.assertIsInstance(self.sut, Conta)
        self.assertEqual(self.descricao1, self.sut.descricao)
        self.assertEqual(self.valor1, self.sut.valor)
        self.assertIsInstance(self.sut.data_recebimento, date)
        self.assertFalse(self.sut.recebida)

    def test_conta_str(self):
        self.assertEqual("R$ 10000 (não recebido)", self.sut.__str__())
