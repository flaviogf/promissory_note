import uuid

from django.test import TestCase
from django.utils import timezone

from api.beneficiarios.models import Beneficiario


class BeneficiarioTests(TestCase):
    def setUp(self):
        self.nome = 'Bruce'
        self.documento = '123'
        self.email = 'batman@email.com'
        self.sut = Beneficiario.objects.create(nome=self.nome,
                                               documento=self.documento,
                                               email=self.email)

    def test_create(self):
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertIsInstance(self.sut.criado_em, timezone.datetime)
        self.assertIsInstance(self.sut.atualizado_em, timezone.datetime)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.documento, self.sut.documento)
        self.assertEqual(self.email, self.sut.email)
