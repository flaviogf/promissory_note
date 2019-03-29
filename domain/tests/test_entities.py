import unittest
import uuid
from datetime import datetime

from domain.entities import Beneficiario, Conta, Emitente, Promisoria
from domain.tests import BeneficiarioFactory, ContaFactory, EmitenteFactory, PromisoriaFactory, fake


class ContaTests(unittest.TestCase):
    def setUp(self):
        self.id = uuid.uuid4()
        self.descricao = fake.sentence()
        self.valor = fake.pyfloat()
        self.data_recebimento = datetime.now()
        self.recebida = fake.pybool()
        self.conta = ContaFactory.build()
        self.sut = Conta(descricao=self.descricao, valor=self.valor)

    def test_init(self):
        self.assertIsInstance(self.sut, Conta)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.descricao, self.sut.descricao)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertIsNone(self.sut.data_recebimento)
        self.assertFalse(self.sut.recebida)

    def test_recebe(self):
        self.sut.recebe()
        self.assertIsInstance(self.sut.data_recebimento, datetime)
        self.assertTrue(self.sut.recebida)

    def test_add(self):
        total_conta = self.sut + self.conta
        total_valor = self.sut.valor + self.conta.valor
        self.assertEqual(total_valor, total_conta)

    def test_factory_cria(self):
        conta = Conta.Factory.cria(id=self.id,
                                   descricao=self.descricao,
                                   valor=self.valor,
                                   data_recebimento=self.data_recebimento,
                                   recebida=self.recebida)

        self.assertEqual(self.id, conta.id)
        self.assertEqual(self.descricao, conta.descricao)
        self.assertEqual(self.valor, conta.valor)
        self.assertEqual(self.data_recebimento, conta.data_recebimento)
        self.assertEqual(self.recebida, conta.recebida)


class PromisoriaTests(unittest.TestCase):
    def setUp(self):
        self.emitente = EmitenteFactory.build()
        self.beneficiario = BeneficiarioFactory.build()
        self.conta = ContaFactory.build()
        self.conta2 = ContaFactory.build()
        self.sut = Promisoria(emitente=self.emitente)

    def test_init(self):
        self.assertIsInstance(self.sut, Promisoria)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.emitente, self.sut.emitente)
        self.assertEqual(None, self.sut.beneficiario)

    def test_adiciona_conta(self):
        self.sut.adiciona_conta(self.conta)
        self.assertEqual(1, len(self.sut.contas))

    def test_iadd(self):
        self.sut += self.conta
        self.assertEqual(1, len(self.sut.contas))

    def test_total(self):
        self.sut += self.conta
        self.sut += self.conta2
        total = self.conta.valor + self.conta2.valor
        self.assertEqual(total, self.sut.total)

    def test_recebe(self):
        self.sut += self.conta
        self.sut.recebe(self.beneficiario)
        for it in self.sut.contas:
            with self.subTest():
                self.assertTrue(it.recebida)

        self.assertTrue(self.sut.recebida)
        self.assertIsInstance(self.sut.data_recebimento, datetime)
        self.assertEqual(self.beneficiario, self.sut.beneficiario)

    def test_dict(self):
        self.sut.recebe(self.beneficiario)
        dicionario_esperado = {
            'emitente': self.sut.emitente.id,
            'beneficiario': self.sut.beneficiario.id,
            'contas': [it.id for it in self.sut.contas],
            'data_recebimento': self.sut.data_recebimento,
            'recebida': self.sut.recebida,
        }
        self.assertDictEqual(dicionario_esperado, self.sut.dict())


class EmitenteTests(unittest.TestCase):
    def setUp(self):
        self.id = uuid.uuid4()
        self.nome = fake.name()
        self.endereco = fake.street_address()
        self.telefone = fake.phone_number()
        self.sut = Emitente(nome=self.nome,
                            endereco=self.endereco,
                            telefone=self.telefone)

    def test_init(self):
        self.assertIsInstance(self.sut, Emitente)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.assertEqual(self.telefone, self.sut.telefone)

    def test_emite_promisoria(self):
        promisoria = self.sut.emite_promisoria()
        self.assertIsInstance(promisoria, Promisoria)
        self.assertEqual(self.sut, promisoria.emitente)

    def test_factory_cria(self):
        emitente = Emitente.Factory.cria(id=self.id,
                                         nome=self.nome,
                                         endereco=self.endereco,
                                         telefone=self.telefone)

        self.assertIsInstance(emitente, Emitente)
        self.assertEqual(self.id, emitente.id)
        self.assertEqual(self.nome, emitente.nome)
        self.assertEqual(self.endereco, emitente.endereco)
        self.assertEqual(self.telefone, emitente.telefone)

    def test_dict(self):
        dicionario_esperado = {
            'id': self.sut.id,
            'nome': self.sut.nome,
            'endereco': self.sut.endereco,
            'telefone': self.sut.telefone,
        }

        self.assertDictEqual(dicionario_esperado, self.sut.dict())


class BeneficiarioTests(unittest.TestCase):
    def setUp(self):
        self.nome = fake.name()
        self.endereco = fake.street_address()
        self.telefone = fake.phone_number()
        self.promisoria = PromisoriaFactory.build()
        self.conta = ContaFactory.build()
        self.promisoria += self.conta
        self.sut = Beneficiario(nome=self.nome,
                                endereco=self.endereco,
                                telefone=self.telefone)

    def test_init(self):
        self.assertIsInstance(self.sut, Beneficiario)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.nome, self.sut.nome)
        self.assertEqual(self.endereco, self.sut.endereco)
        self.assertEqual(self.telefone, self.sut.telefone)
        self.assertEqual(0, len(self.sut.promisorias_recebidas))

    def test_recebe(self):
        self.sut.recebe(self.promisoria)
        self.assertEqual(1, len(self.sut.promisorias_recebidas))
        for it in self.sut.promisorias_recebidas:
            with self.subTest():
                self.assertTrue(it.recebida)

    def test_factory_cria(self):
        beneficiario = Beneficiario.Factory.cria(id=self.id,
                                                 nome=self.nome,
                                                 endereco=self.endereco,
                                                 telefone=self.telefone)

        self.assertIsInstance(beneficiario, Beneficiario)
        self.assertEqual(self.id, beneficiario.id)
        self.assertEqual(self.nome, beneficiario.nome)
        self.assertEqual(self.endereco, beneficiario.endereco)
        self.assertEqual(self.telefone, beneficiario.telefone)

    def test_dict(self):
        dicionario_esperado = {
            'id': self.sut.id,
            'nome': self.sut.nome,
            'endereco': self.sut.endereco,
            'telefone': self.sut.telefone,
        }

        self.assertDictEqual(dicionario_esperado, self.sut.dict())
