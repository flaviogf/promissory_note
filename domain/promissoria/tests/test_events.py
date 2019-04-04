import unittest
from datetime import datetime

from domain.promissoria.events import PromissoriaEmitidaEvent


class PromissoriaEmitidaEventTests(unittest.TestCase):
    def setUp(self):
        self.numero = '1'
        self.data_vencimento = datetime.now()
        self.valor = 10
        self.nome_beneficiario = "Bruce"
        self.documento_beneficiario = "123"
        self.email_beneficiario = "batman@dc.com"
        self.nome_emitente = "Peter"
        self.documento_emitente = "456"
        self.email_emitente = "aranha-humana@marvel.com"
        self.endereco_emitente = "Brooklyn"
        self.data_emissao = datetime.now()
        self.recebida = True
        self.sut = PromissoriaEmitidaEvent(numero=self.numero,
                                           data_vencimento=self.data_vencimento,
                                           valor=self.valor,
                                           nome_beneficiario=self.nome_beneficiario,
                                           documento_beneficiario=self.documento_beneficiario,
                                           email_beneficiario=self.email_beneficiario,
                                           nome_emitente=self.nome_emitente,
                                           documento_emitente=self.documento_emitente,
                                           email_emitente=self.email_emitente,
                                           endereco_emitente=self.endereco_emitente,
                                           data_emissao=self.data_emissao,
                                           recebida=self.recebida)

    def test_init(self):
        self.assertEqual(self.numero, self.sut.numero)
        self.assertEqual(self.data_vencimento, self.sut.data_vencimento)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertEqual(self.nome_beneficiario, self.sut.nome_beneficiario)
        self.assertEqual(self.documento_beneficiario, self.sut.documento_beneficiario)
        self.assertEqual(self.email_beneficiario, self.sut.email_beneficiario)
        self.assertEqual(self.nome_emitente, self.sut.nome_emitente)
        self.assertEqual(self.documento_emitente, self.sut.documento_emitente)
        self.assertEqual(self.email_emitente, self.sut.email_emitente)
        self.assertEqual(self.endereco_emitente, self.sut.endereco_emitente)
        self.assertEqual(self.data_emissao, self.sut.data_emissao)
        self.assertEqual(self.recebida, self.sut.recebida)
