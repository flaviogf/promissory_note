"""modulo de testes das models do app beneficarios"""
from django.test import TestCase

from api.beneficiarios.models import BeneficiarioModel
from api.beneficiarios.tests import fake


class BeneficiarioModelTests(TestCase):
    """classe responsavel pelos testes da classe BeneficiarioModel"""
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.address()
        self.telefone = fake.phone_number()
        self.sut = BeneficiarioModel.objects.create(nome=self.nome,
                                                    endereco=self.endereco,
                                                    telefone=self.telefone)

    def test_create(self):
        """testa o metodo create"""
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.assertEqual(self.telefone, self.sut.telefone)
