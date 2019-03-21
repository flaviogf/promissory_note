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
        self.sut.contas.add(self.conta1)

    def test_promisoria_create(self):
        self.assertEqual(self.contato1, self.sut.contato)
        self.assertEqual(self.endereco1, self.sut.endereco)
        self.assertEqual(1, self.sut.contas.count())
