import unittest

from promissoria.application.commands import CadastrarEmitenteCommand


class CadastrarEmitenteCommandTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.nome = 'steve rogers'
        self.cpf = '12312312312'
        self.endereco = 'new york'
        self.sut = CadastrarEmitenteCommand(nome=self.nome,
                                            cpf=self.cpf,
                                            endereco=self.endereco)

    def test_init(self) -> 'None':
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.cpf, self.sut.cpf)
        self.assertEqual(self.endereco, self.sut.endereco)
