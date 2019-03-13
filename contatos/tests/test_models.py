from django.test import TestCase
from faker import Faker

from contatos.models import Contato

fake = Faker('pt_PT')


class ContatoTests(TestCase):
    def setUp(self):
        self.nome1 = fake.name()
        self.email1 = fake.email()
        self.telefone1 = fake.phone_number()

        self.sut = Contato.objects.create(
            nome=self.nome1, email=self.email1, telefone=self.telefone1)

    def test_contato_create(self):
        self.assertIsInstance(self.sut, Contato)
        self.assertEqual(self.nome1, self.sut.nome)
        self.assertEqual(self.email1, self.sut.email)
        self.assertEqual(self.telefone1, self.sut.telefone)

    def test_contato_str(self):
        self.assertEqual(self.nome1, self.sut.__str__())
