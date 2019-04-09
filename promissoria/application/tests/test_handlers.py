import unittest
from unittest.mock import patch, Mock

from promissoria.application.commands import CadastrarEmitenteCommand
from promissoria.application.handlers import CadastrarEmitente


class CadastrarEmitenteTests(unittest.TestCase):
    @patch('promissoria.domain.repositories.EmitenteRepository')
    def setUp(self, emitente_repository: 'Mock') -> 'None':
        self.emitente_repository = emitente_repository
        self.nome = 'steve'
        self.cpf = '11122233311'
        self.endereco = 'new york'
        self.command = CadastrarEmitenteCommand(nome=self.nome,
                                                cpf=self.cpf,
                                                endereco=self.endereco)
        self.sut = CadastrarEmitente(emitente_repository=self.emitente_repository)

    def test_handle(self) -> 'None':
        self.sut.handle(self.command)
        self.emitente_repository.salva.assert_called_once()


class CadastarBeneficiarioTests(unittest.TestCase):
    pass
