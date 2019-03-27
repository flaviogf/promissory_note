from django.test import TestCase

from api.beneficiarios.repositories import DjangoBeneficiarioRepository
from api.beneficiarios.tests import BeneficiarioModelFactory
from domain.entities import Beneficiario


class DjangoBeneficiarioRepositoryTests(TestCase):
    def setUp(self):
        self.beneficiario1 = BeneficiarioModelFactory.create()
        self.beneficiario2 = BeneficiarioModelFactory.create()
        self.sut = DjangoBeneficiarioRepository()

    def test_busca_por_id(self):
        beneficiario = self.sut.busca_por_id(self.beneficiario1.id)
        self.assertIsInstance(beneficiario, Beneficiario)
        self.assertEqual(self.beneficiario1.id, beneficiario.id)
        self.assertEqual(self.beneficiario1.nome, beneficiario.nome)
        self.assertEqual(self.beneficiario1.endereco, beneficiario.endereco)
        self.assertEqual(self.beneficiario1.telefone, beneficiario.telefone)
