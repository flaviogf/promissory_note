import unittest

from domain.commands import CriarPromisoriaCommand


class CriarPromisoriaCommandTests(unittest.TestCase):
    def setUp(self):
        self.sut = CriarPromisoriaCommand()

    def test_init(self):
        self.assertIsNone(self.sut.id_emitente)
        self.assertIsNone(self.sut.id_beneficario)
        self.assertEqual(0, len(self.sut.id_contas))
