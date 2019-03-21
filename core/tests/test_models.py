from datetime import date

import factory
from django.test import TestCase

from core.models import Promisoria
from core.tests import ContaFactory, ContatoFactory, EnderecoFactory


class PromisoriaTests(TestCase):
    def setUp(self):
        self.contato1 = ContatoFactory.create()
        self.endereco1 = EnderecoFactory.create()
        self.conta1 = ContaFactory.create()
        self.conta2 = ContaFactory.create()

        self.sut = Promisoria.objects.create(
            contato=self.contato1, endereco=self.endereco1)
        self.sut.adiciona_conta(self.conta1)

    def test_promisoria_create(self):
        self.assertEqual(self.contato1, self.sut.contato)
        self.assertEqual(self.endereco1, self.sut.endereco)
        self.assertEqual(1, self.sut.quantidade_de_contas)

    def test_promisoria_str_(self):
        self.assertEqual('contas 1 (não recebida)', self.sut.__str__())

    def test_promisoria_adiciona_conta(self):
        self.sut.adiciona_conta(self.conta2)
        self.assertEqual(2, self.sut.quantidade_de_contas)

    def test_promisoria_quantidade_de_contas(self):
        self.assertEqual(1, self.sut.quantidade_de_contas)

    def test_promisoria_baixa(self):
        self.sut.baixa()
        self.assertTrue(self.sut.recebida)
        self.assertEqual(date.today(), self.sut.data_recebimento)
        for it in self.sut.contas.all():
            with self.subTest():
                self.assertTrue(it.recebida)
