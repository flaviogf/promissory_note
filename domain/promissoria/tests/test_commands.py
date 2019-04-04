import unittest
import uuid
from datetime import datetime

from domain.promissoria.commands import SolicitarPromissoriaCommand


class SolicitarPromissoriaCommandTests(unittest.TestCase):
    def setUp(self):
        self.numero = '1'
        self.data_vencimento = datetime.now()
        self.valor = 10
        self.id_beneficiario = uuid.uuid4()
        self.id_emitente = uuid.uuid4()
        self.sut = SolicitarPromissoriaCommand(numero=self.numero,
                                               data_vencimento=self.data_vencimento,
                                               valor=self.valor,
                                               id_beneficiario=self.id_beneficiario,
                                               id_emitente=self.id_emitente)

    def test_init(self):
        self.assertEqual(self.numero, self.sut.numero)
        self.assertEqual(self.data_vencimento, self.sut.data_vencimento)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertEqual(self.id_beneficiario, self.sut.id_beneficiario)
        self.assertEqual(self.id_emitente, self.sut.id_emitente)
