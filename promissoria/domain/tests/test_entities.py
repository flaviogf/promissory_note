import unittest
import uuid
from unittest.mock import patch, Mock

from promissoria.domain.entities import Emitente, Beneficiario


class EmitenteTests(unittest.TestCase):
    @patch('promissoria.domain.entities.EventPublisher')
    def setUp(self, publisher: 'Mock') -> 'None':
        self.publisher = publisher
        self.nome = 'tony'
        self.cpf = '12345678900'
        self.endereco = 'Rua x'
        self.sut = Emitente.novo(nome=self.nome,
                                 cpf=self.cpf,
                                 endereco=self.endereco)

    def test_novo(self) -> 'None':
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.cpf, self.sut.cpf)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.publisher.instancia().publish.assert_called_once()


class BeneficiarioTests(unittest.TestCase):
    @patch('promissoria.domain.entities.EventPublisher')
    def setUp(self, publisher: 'Mock') -> 'None':
        self.publiser = publisher
        self.nome = 'steve'
        self.cpf = '12312312311'
        self.sut = Beneficiario.novo(nome=self.nome,
                                     cpf=self.cpf)

    def test_novo(self) -> 'None':
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.cpf, self.sut.cpf)
