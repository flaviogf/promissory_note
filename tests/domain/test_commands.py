import unittest

from domain.commands import EmitirPromisoriaCommand


class EmitirPromisoriaCommandTests(unittest.TestCase):
    def setUp(self):
        self.sut = EmitirPromisoriaCommand()

    def test_init(self):
        self.assertIsNone(self.sut.id_emitente)
        self.assertIsNone(self.sut.id_beneficario)
        self.assertEqual(0, len(self.sut.id_contas))
