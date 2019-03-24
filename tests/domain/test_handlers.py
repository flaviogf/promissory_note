import unittest
import uuid

from domain.commands import CriarPromisoriaCommand, CriarPromisoriaCommandResult
from domain.handlers import CriarPromisoriaHandler
from tests.domain import (BeneficiarioRepositoryMock, ContaRepositoryMock, EmitenteRepositoryMock,
                          PromisoriaRepositoryMock)


class CriarPromisoriaHandlerTests(unittest.TestCase):
    def setUp(self):
        self.command = CriarPromisoriaCommand()
        self.command.id_emitente = uuid.uuid4()
        self.command.id_beneficario = uuid.uuid4()
        self.command.id_contas = [uuid.uuid4()]

        self.sut = CriarPromisoriaHandler(EmitenteRepositoryMock(),
                                          BeneficiarioRepositoryMock(),
                                          ContaRepositoryMock(),
                                          PromisoriaRepositoryMock())

    def test_handle(self):
        command_result = self.sut.handle(self.command)
        self.assertIsInstance(command_result, CriarPromisoriaCommandResult)
        self.assertTrue(command_result.status)
