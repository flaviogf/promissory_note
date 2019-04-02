from datetime import datetime

from django.test import TestCase

from api.beneficiarios.models import Beneficiario as BeneficiarioData
from api.emitentes.models import Emitente as EmitenteData
from api.promissorias.models import Promissoria as PromissoriaData
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
        BeneficiarioData.objects.create(id=self.beneficiario.id,
                                        nome=self.beneficiario.nome,
                                        documento=self.beneficiario.documento,
                                        email=self.beneficiario.email)

        self.emitente = Emitente(nome='Bruce',
                                 documento='123',
                                 endereco='gotham',
                                 email='batman@dc.com')

        EmitenteData.objects.create(id=self.emitente.id,
                                    nome=self.emitente.nome,
                                    documento=self.emitente.documento,
                                    email=self.emitente.email,
                                    endereco=self.emitente.endereco)

        self.promissoria = Promissoria(numero=self.numero,
                                       data_vencimento=self.data_vencimento,
                                       valor=self.valor,
                                       beneficiario=self.beneficiario,
                                       emitente=self.emitente)

        self.sut = DjangoPromissoriaRepository()

    def test_insere(self):
        self.sut.insere(self.promissoria)
        self.assertEqual(1, PromissoriaData.objects.count())
