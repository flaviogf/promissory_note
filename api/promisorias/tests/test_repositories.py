"""modulo de testes dos repositorios do app promisorias"""
from django.test import TestCase

from api.beneficiarios.tests import BeneficiarioModelFactory
from api.contas.tests import ContaModelFactory
from api.emitentes.tests import EmitenteModelFactory
from api.promisorias.models import PromisoriaModel
from api.promisorias.repositories import DjangoPromisoriaRepository
from domain.entities import Beneficiario, Conta, Emitente


class DjangoPromisoriaRepositoryTest(TestCase):
    """classe responsavel pelos testes da classe DjangoPromisoriaRepository"""
    def setUp(self):
        emitente_model = EmitenteModelFactory.create()
        beneficiario_model = BeneficiarioModelFactory.create()
        contas_model = ContaModelFactory.create_batch(10)
        self.emitente = Emitente.Factory.cria(id=emitente_model.id,
                                              nome=emitente_model.nome,
                                              endereco=emitente_model.endereco,
                                              telefone=emitente_model.telefone)
        self.beneficiario = Beneficiario.Factory.cria(id=beneficiario_model.id,
                                                      nome=beneficiario_model.nome,
                                                      endereco=beneficiario_model.endereco,
                                                      telefone=beneficiario_model.telefone)
        self.contas = [Conta.Factory.cria(id=it.id,
                                          descricao=it.descricao,
                                          valor=it.valor,
                                          data_recebimento=it.data_recebimento,
                                          recebida=it.recebida) for it in contas_model]

        self.promisoria = self.emitente.emite_promisoria()

        for it in self.contas:
            self.promisoria += it

        self.beneficiario.recebe(self.promisoria)
        self.sut = DjangoPromisoriaRepository()

    def test_insere(self):
        """testa o metodo insere"""
        self.sut.insere(self.promisoria)
        promisoria_inserida = PromisoriaModel.objects.reverse()[0]
        self.assertEqual(1, PromisoriaModel.objects.count())
        self.assertEqual(len(self.contas), promisoria_inserida.contas.count())
