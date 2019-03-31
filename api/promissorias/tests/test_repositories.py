from datetime import datetime

from django.test import TestCase

from api.promissorias import models
from api.promissorias.repositories import DjangoPromissoriaRepository
from domain.core.entities import Beneficiario, Emitente, Promissoria


class DjangoPromissoriaRepositoryTests(TestCase):
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
        self.promissoria = Promissoria(numero=self.numero,
                                       data_vencimento=self.data_vencimento,
                                       valor=self.valor,
                                       beneficiario=self.beneficiario,
                                       emitente=self.emitente)

        self.sut = DjangoPromissoriaRepository()

    def test_insere(self):
        self.sut.insere(self.promissoria)
        self.assertEqual(1, models.Promissoria.objects.count())
