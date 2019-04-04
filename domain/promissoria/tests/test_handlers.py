import unittest
import uuid
from datetime import datetime
from unittest import mock

from domain.promissoria.commands import SolicitarPromissoriaCommand
from domain.promissoria.events import PromissoriaEmitidaEvent
from domain.promissoria.handlers import SolicitarPromissoriaHandler, PromissoriaEmitidaHandler
from domain.promissoria.repositories import EmitenteRepository, BeneficiarioRepository, PromissoriaRepository
from domain.promissoria.services import EmailService


class SolicitarPromissoriaHandlerTests(unittest.TestCase):

    @mock.patch('domain.promissoria.repositories.EmitenteRepository')
    @mock.patch('domain.promissoria.repositories.BeneficiarioRepository')
    @mock.patch('domain.promissoria.repositories.PromissoriaRepository')
    @mock.patch('domain.promissoria.handlers.PromissoriaEmitidaHandler')
    def setUp(self,
              mock_emitente_repository: 'EmitenteRepository',
              mock_beneficiario_repository: 'BeneficiarioRepository',
              mock_promissoria_repository: 'PromissoriaRepository',
              mock_promissoria_emitida_handler: 'PromissoriaEmitidaHandler'):
        self.mock_emitente_repository = mock_emitente_repository
        self.mock_beneficiario_repository = mock_beneficiario_repository
        self.mock_promissoria_repository = mock_promissoria_repository
        self.mock_promissoria_emitida_handler = mock_promissoria_emitida_handler

        self.command = SolicitarPromissoriaCommand(numero='1',
                                                   data_vencimento=datetime.now(),
                                                   valor=100,
                                                   id_beneficiario=uuid.uuid4(),
                                                   id_emitente=uuid.uuid4())

        self.sut = SolicitarPromissoriaHandler(emitente_repository=self.mock_emitente_repository,
                                               beneficiario_repository=self.mock_beneficiario_repository,
                                               promissoria_repository=self.mock_promissoria_repository,
                                               promissoria_emitida_handler=self.mock_promissoria_emitida_handler)

    def test_handle(self):
        self.sut.handle(self.command)

        self.mock_emitente_repository.busca_por_id.assert_called_with(self.command.id_emitente)
        self.mock_beneficiario_repository.busca_por_id.assert_called_with(self.command.id_beneficiario)
        self.mock_promissoria_repository.insere.assert_called_once()
        self.mock_promissoria_emitida_handler.send.assert_called_once()


class PromissoriaEmitidaHandlerTests(unittest.TestCase):

    @mock.patch('domain.promissoria.services.EmailService')
    def setUp(self, mock_email_service: 'EmailService'):
        self.mock_email_service = mock_email_service

        self.event = PromissoriaEmitidaEvent(numero='1',
                                             data_vencimento=datetime.now(),
                                             valor=10,
                                             nome_beneficiario='Bruce',
                                             documento_beneficiario='123',
                                             email_beneficiario='bruce@wayne.com',
                                             nome_emitente='peter',
                                             documento_emitente='456',
                                             email_emitente='peter@email.com',
                                             endereco_emitente='new york',
                                             data_emissao=datetime.now(),
                                             recebida=False)

        self.sut = PromissoriaEmitidaHandler(email_service=self.mock_email_service)

    def test_send(self):
        self.sut.send(self.event)

        email_beneficiario = mock.call(self.event.email_beneficiario,
                                       'Uma promissoria foi emitida para você')

        email_emitente = mock.call(self.event.email_emitente,
                                   'Uma promissoria foi emitida em seu nome')

        self.mock_email_service.envia.assert_has_calls([email_beneficiario, email_emitente])
