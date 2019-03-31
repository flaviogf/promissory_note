import uuid

from django.test import TestCase
from django.utils import timezone

from api.promissorias.models import Promissoria


class PromissoriaTests(TestCase):
    def setUp(self):
        self.numero = 1
        self.data_vencimento = timezone.now()
        self.valor = 100
        self.beneficiario = None
        self.emitente = None

        self.sut = Promissoria.objects.create(numero=self.numero,
                                              data_vencimento=self.data_vencimento,
                                              valor=self.valor,
                                              beneficiario=self.beneficiario,
                                              emitente=self.emitente)

    def test_create(self):
        self.assertIsInstance(self.sut, Promissoria)
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertEqual(self.data_vencimento, self.sut.data_vencimento)
        self.assertEqual(self.valor, self.sut.valor)
        self.assertEqual(self.beneficiario, self.sut.beneficiario)
        self.assertEqual(self.emitente, self.sut.emitente)
        self.assertIsInstance(self.sut.data_emissao, timezone.datetime)
        self.assertFalse(self.sut.recebida)
