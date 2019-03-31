from django.test import TestCase

from api.beneficiarios import models
from api.beneficiarios.repositories import DjangoBeneficiarioRepository
from domain.core.entities import Beneficiario


class DjangoBeneficiarioRepositoryTests(TestCase):
    def setUp(self):
        self.beneficiario = models.Beneficiario.objects.create(nome='Bruce',
                                                               documento='123',
                                                               email='batman@email.com')

        self.sut = DjangoBeneficiarioRepository()

    def test_busca_por_id(self):
        beneficiario = self.sut.busca_por_id(self.beneficiario.id)
        self.assertIsInstance(beneficiario, Beneficiario)
