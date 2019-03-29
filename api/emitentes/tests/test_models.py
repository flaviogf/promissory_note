import uuid

from django.test import TestCase

from api.emitentes.models import EmitenteModel
from api.emitentes.tests import fake


class EmitenteModelTests(TestCase):
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.address()
        self.telefone = fake.phone_number()
        self.sut = EmitenteModel.objects.create(nome=self.nome,
                                                endereco=self.endereco,
                                                telefone=self.telefone)

    def test_create(self):
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.assertEqual(self.telefone, self.sut.telefone)

    def test_str(self):
        self.assertEqual(self.nome, self.sut.__str__())
