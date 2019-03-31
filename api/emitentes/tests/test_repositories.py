from django.test import TestCase

from api.emitentes import models
from api.emitentes.repositories import DjangoEmitenteRepository
from domain.core.entities import Emitente


class DjangoEmitenteRepositoryTests(TestCase):
    def setUp(self):
        self.emitente = models.Emitente.objects.create(nome='Bruce',
                                                       documento='123',
                                                       email='batman@email.com',
                                                       endereco='gotham')

        self.sut = DjangoEmitenteRepository()

    def test_busca_por_id(self):
        emitente = self.sut.busca_por_id(self.emitente.id)
        self.assertIsInstance(emitente, Emitente)
