from django.test import TestCase
from tests.domain import PromisoriaFactory

from api.promisorias.models import PromisoriaModel
from api.promisorias.repositories import DjangoPromisoriaRepository


class DjangoPromisoriaRepositoryTest(TestCase):
    def setUp(self):
        self.promisoria = PromisoriaFactory.create()
        self.sut = DjangoPromisoriaRepository()

    def test_insere(self):
        self.sut.insere(self.promisoria)
        self.assertEqual(1, PromisoriaModel.objects.count())
