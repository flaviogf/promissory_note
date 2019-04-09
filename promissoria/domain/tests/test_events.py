import unittest
import uuid

from promissoria.domain.events import EmitenteCadastrado, BeneficiarioCadastrado


class EmitenteCadastradoTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.nome = 'steve rogers'
        self.cpf = '12345678912'
        self.endereco = 'Rua x'
        self.sut = EmitenteCadastrado(nome=self.nome,
                                      cpf=self.cpf,
                                      endereco=self.endereco)

    def test_init(self) -> 'None':
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.cpf, self.sut.cpf)
        self.assertEqual(self.endereco, self.sut.endereco)


class BeneficiarioCadastradoTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.nome = 'steve'
        self.cpf = '12312312311'
        self.sut = BeneficiarioCadastrado(nome=self.nome,
                                          cpf=self.cpf)

    def test_init(self) -> 'None':
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.cpf, self.sut.cpf)
