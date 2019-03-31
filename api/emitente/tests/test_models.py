import uuid

from django.test import TestCase
from django.utils import timezone

from api.emitente.models import Emitente


class EmitenteTests(TestCase):
    def setUp(self):
        self.nome = 'Bruce'
        self.documento = '123'
        self.email = 'batman@email.com'
        self.endereco = 'gotham'
        self.sut = Emitente.objects.create(nome=self.nome,
                                           documento=self.documento,
                                           email=self.email,
                                           endereco=self.endereco)

    def test_create(self):
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertIsInstance(self.sut.criado_em, timezone.datetime)
        self.assertIsInstance(self.sut.atualizado_em, timezone.datetime)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.documento, self.sut.documento)
        self.assertEqual(self.email, self.sut.email)
        self.assertEqual(self.endereco, self.sut.endereco)
