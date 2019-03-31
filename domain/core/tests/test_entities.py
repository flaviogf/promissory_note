import unittest
import uuid
from datetime import datetime

from domain.core.entities import Promissoria, Emitente, Beneficiario


class PromissoriaTests(unittest.TestCase):
    def setUp(self):
        self.numero = '1'
        self.data_vencimento = datetime.now()
        self.valor = 10
        self.beneficiario = Beneficiario(nome='Peter',
                                         documento='456',
                                         email='aranha-humana@marvel.com')
        self.emitente = Emitente(nome='Bruce',
                                 documento='123',
                                 endereco='gotham',
                                 email='batman@dc.com')
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
        self.assertIsInstance(self.sut.emitente, Emitente)
        self.assertEqual(self.emitente, self.sut.emitente)
        self.assertIsInstance(self.sut.data_emissao, datetime)
        self.assertFalse(self.sut.recebida)


class EmitenteTests(unittest.TestCase):
    def setUp(self):
        self.nome = 'Bruce'
        self.documento = '123'
        self.endereco = 'gotham'
        self.email = 'batman@dc.com.br'
        self.numero = '1'
        self.data_vencimento = datetime.now()
        self.valor = 10
        self.beneficiario = Beneficiario(nome='Peter',
                                         documento='456',
                                         email='aranha-humana@marvel.com')
        self.sut = Emitente(nome=self.nome,
                            documento=self.documento,
                            email=self.email,
                            endereco=self.endereco)

    def test_init(self):
        self.assertIsInstance(self.sut, Emitente)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.documento, self.sut.documento)
        self.assertEqual(self.email, self.sut.email)
        self.assertEqual(self.endereco, self.sut.endereco)

    def test_emite_promissoria(self):
        promissoria = self.sut.emite_promissoria(numero=self.numero,
                                                 data_vencimento=self.data_vencimento,
                                                 valor=self.valor,
                                                 beneficiario=self.beneficiario)
        self.assertIsInstance(promissoria, Promissoria)
        self.assertIsInstance(promissoria.id, uuid.UUID)
        self.assertEqual(self.numero, promissoria.numero)
        self.assertEqual(self.data_vencimento, promissoria.data_vencimento)
        self.assertEqual(self.valor, promissoria.valor)
        self.assertEqual(self.beneficiario, promissoria.beneficiario)
        self.assertIsInstance(promissoria.emitente, Emitente)
        self.assertEqual(self.sut, promissoria.emitente)
        self.assertIsInstance(promissoria.data_emissao, datetime)
        self.assertFalse(promissoria.recebida)

    def test_factory_cria(self):
        emitente = Emitente.Factory.cria(id=uuid.uuid4(),
                                         nome=self.nome,
                                         documento=self.documento,
                                         email=self.email,
                                         endereco=self.endereco)

        self.assertIsInstance(emitente, Emitente)
        self.assertIsInstance(emitente.id, uuid.UUID)
        self.assertEqual(self.nome, emitente.nome)
        self.assertEqual(self.documento, emitente.documento)
        self.assertEqual(self.email, emitente.email)
        self.assertEqual(self.endereco, self.sut.endereco)


class BenficiarioTests(unittest.TestCase):
    def setUp(self):
        self.nome = 'Peter'
        self.documento = '456'
        self.email = 'aranha-humana@marvel.com'
        self.sut = Beneficiario(nome=self.nome,
                                documento=self.documento,
                                email=self.email)

    def test_init(self):
        self.assertIsInstance(self.sut, Beneficiario)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.documento, self.sut.documento)
        self.assertEqual(self.email, self.sut.email)

    def test_factory_cria(self):
        beneficiario = Beneficiario.Factory.cria(id=uuid.uuid4(),
                                                 nome=self.nome,
                                                 documento=self.documento,
                                                 email=self.email)

        self.assertIsInstance(beneficiario, Beneficiario)
        self.assertIsInstance(beneficiario.id, uuid.UUID)
        self.assertEqual(self.nome, beneficiario.nome)
        self.assertEqual(self.documento, beneficiario.documento)
        self.assertEqual(self.email, beneficiario.email)
