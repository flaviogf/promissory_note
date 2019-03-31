import unittest
import uuid
from datetime import datetime
from unittest import mock

from domain.core.commands import SolicitarPromissoriaCommand
from domain.core.handlers import SolicitarPromissoriaHandler
from domain.core.repositories import EmitenteRepository, BeneficiarioRepository, PromissoriaRepository


class SolicitarPromissoriaHandlerTests(unittest.TestCase):

    @mock.patch('domain.core.repositories.EmitenteRepository')
    @mock.patch('domain.core.repositories.BeneficiarioRepository')
    @mock.patch('domain.core.repositories.PromissoriaRepository')
    def setUp(self,
              mock_emitente_repository: 'EmitenteRepository',
              mock_beneficiario_repository: 'BeneficiarioRepository',
              mock_promissoria_repository: 'PromissoriaRepository'):
        self.mock_emitente_repository = mock_emitente_repository
        self.mock_beneficiario_repository = mock_beneficiario_repository
        self.mock_promissoria_repository = mock_promissoria_repository

        self.command = SolicitarPromissoriaCommand(numero='1',
                                                   data_vencimento=datetime.now(),
                                                   valor=100,
                                                   id_beneficiario=uuid.uuid4(),
                                                   id_emitente=uuid.uuid4())

        self.sut = SolicitarPromissoriaHandler(emitente_repository=self.mock_emitente_repository,
                                               beneficiario_repository=self.mock_beneficiario_repository,
                                               promissoria_repository=self.mock_promissoria_repository)

    def test_handle(self):
        self.sut.handle(self.command)

        self.mock_emitente_repository.busca_por_id.assert_called_with(self.command.id_emitente)
        self.mock_beneficiario_repository.busca_por_id.assert_called_with(self.command.id_beneficiario)
        self.mock_promissoria_repository.insere.assert_called_once()
