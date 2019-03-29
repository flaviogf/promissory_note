import unittest
import uuid

from domain.commands import EmitirPromisoriaCommand, EmitirPromisoriaCommandResult
from domain.handlers import EmitirPromisoriaHandler
from domain.tests import (BeneficiarioRepositoryMock, ContaRepositoryMock, EmitenteRepositoryMock,
                          PromisoriaRepositoryMock)


class EmitirPromisoriaHandlerTests(unittest.TestCase):
    def setUp(self):
        self.command = EmitirPromisoriaCommand()
        self.command.id_emitente = uuid.uuid4()
        self.command.id_beneficario = uuid.uuid4()
        self.command.id_contas = [uuid.uuid4()]

        self.sut = EmitirPromisoriaHandler(EmitenteRepositoryMock(),
                                           BeneficiarioRepositoryMock(),
                                           ContaRepositoryMock(),
                                           PromisoriaRepositoryMock())

    def test_handle(self):
        command_result = self.sut.handle(self.command)
        self.assertIsInstance(command_result, EmitirPromisoriaCommandResult)
        self.assertTrue(command_result.status)
