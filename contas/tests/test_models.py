from datetime import datetime, timedelta

from django.test import TestCase

from contas.models import Conta
from contatos.models import Contato


class TestConta(TestCase):
    def setUp(self):
        self.contato = Contato.objects.create(
            nome='Flavio', email='flavio@email.com', telefone='016999999999')

    def test_conta_create(self):
        data_recebimento_esperado = datetime.now() - timedelta(days=2)
        data_recebimento = datetime.now() - timedelta(days=1)

        conta = Conta.objects.create(contato=self.contato,
                      valor=100.0,
                      data_recebimento_esperado=data_recebimento_esperado,
                      data_recebimento=data_recebimento)

        self.assertEqual(self.contato, conta.contato)
        self.assertEqual(100.0, conta.valor)
        self.assertEqual(data_recebimento_esperado,
                         conta.data_recebimento_esperado)
        self.assertEqual(data_recebimento, conta.data_recebimento)

    def test_conta_recebida(self):
        data_recebimento_esperado = datetime.now() - timedelta(days=2)
        data_recebimento = datetime.now() - timedelta(days=1)

        conta = Conta.objects.create(contato=self.contato,
                      valor=100.0,
                      data_recebimento_esperado=data_recebimento_esperado,
                      data_recebimento=data_recebimento)

        self.assertTrue(conta.recebida)

    def test_conta_vencida(self):
        data_recebimento_esperado = datetime.now() - timedelta(days=2)
        data_recebimento = datetime.now() - timedelta(days=1)

        conta = Conta.objects.create(contato=self.contato,
                      valor=100.0,
                      data_recebimento_esperado=data_recebimento_esperado,
                      data_recebimento=data_recebimento)

        self.assertFalse(conta.vencida)

    def test_conta_recebe(self):
        data_recebimento_esperado = datetime.now() - timedelta(days=2)

        conta = Conta.objects.create(contato=self.contato, valor=100.0,
                      data_recebimento_esperado=data_recebimento_esperado)

        conta.recebe()

        self.assertTrue(conta.recebida)

    def test_conta_recebe_passando_data_recebimento(self):
        data_recebimento_esperado = datetime.now() - timedelta(days=2)
        data_recebimento = datetime.now() - timedelta(days=1)

        conta = Conta.objects.create(contato=self.contato,
                      valor=100.0,
                      data_recebimento_esperado=data_recebimento_esperado)

        conta.recebe(data_recebimento=data_recebimento)

        self.assertEqual(data_recebimento, conta.data_recebimento)
        self.assertTrue(conta.recebida)
