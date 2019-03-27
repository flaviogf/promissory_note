from django.test import TestCase

from api.emitentes.repositories import DjangoEmitenteRepository
from api.emitentes.tests import EmitenteModelFactory
from domain.entities import Emitente


class DjangoEmitenteRepositoryTests(TestCase):
    def setUp(self):
        self.emitente1 = EmitenteModelFactory.create()
        self.emitente2 = EmitenteModelFactory.create()
        self.sut = DjangoEmitenteRepository()

    def test_busca_por_id(self):
        id = self.emitente1.id
        emitente = self.sut.busca_por_id(id)
        self.assertIsInstance(emitente, Emitente)
        self.assertEqual(self.emitente1.id, emitente.id)
        self.assertEqual(self.emitente1.nome, emitente.nome)
        self.assertEqual(self.emitente1.endereco, emitente.endereco)
        self.assertEqual(self.emitente1.telefone, emitente.telefone)
