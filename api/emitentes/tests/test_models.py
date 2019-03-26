"""modulo de test das models do app emitentes"""
import uuid

from django.test import TestCase

from api.emitentes.models import EmitenteData
from api.emitentes.tests import fake


class EmitenteDataTests(TestCase):
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.address()
        self.telefone = fake.phone_number()
        self.sut = EmitenteData.objects.create(nome=self.nome,
                                               endereco=self.endereco,
                                               telefone=self.telefone)

    def test_init(self):
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.assertEqual(self.telefone, self.sut.telefone)