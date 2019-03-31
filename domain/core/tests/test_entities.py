import unittest
import uuid
from datetime import datetime

from domain.core.entities import Promissoria


class PromissoriaTests(unittest.TestCase):
    def setUp(self):
        self.numero = 1
        self.data_vencimento = datetime.now()
        self.valor = 10
        self.beneficiario = None
        self.emitente = None
        self.sut = Promissoria(numero=self.numero,
                               data_vencimento=self.data_vencimento,
                               valor=self.valor,
                               beneficiario=self.beneficiario,
                               emitente=self.emitente)

    def test_init(self):
        self.assertIsInstance(self.sut, Promissoria)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.numero, self.sut.numero)
        self.assertEqual(self.data_vencimento, self.sut.data_vencimento)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertEqual(self.beneficiario, self.sut.beneficiario)
        self.assertEqual(self.emitente, self.sut.emitente)
        self.assertIsInstance(self.sut.data_emissao, datetime)
        self.assertFalse(self.sut.recebida)
