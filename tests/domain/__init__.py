from typing import List

import factory
from faker import Faker

from domain.entities import Beneficiario, Conta, Emitente, Promisoria
from domain.repositories import BeneficiarioRepository, ContaRepository, EmitenteRepository, PromisoriaRepository

fake = Faker('pt_BR')


class EmitenteFactory(factory.Factory):
    class Meta:
        model = Emitente

    nome = factory.Faker('name')
    endereco = factory.Faker('street_address')
    telefone = factory.Faker('phone_number')


class BeneficiarioFactory(factory.Factory):
    class Meta:
        model = Beneficiario

    nome = factory.Faker('name')
    endereco = factory.Faker('street_address')
    telefone = factory.Faker('phone_number')


class ContaFactory(factory.Factory):
    class Meta:
        model = Conta

    descricao = factory.Faker('sentence')
    valor = factory.Faker('pyfloat')


class PromisoriaFactory(factory.Factory):
    class Meta:
        model = Promisoria

    emitente = EmitenteFactory.build()


class EmitenteRepositoryMock(EmitenteRepository):
    def busca_por_id(self, id: 'UUID') -> 'Emitente':
        return EmitenteFactory.build()


class BeneficiarioRepositoryMock(BeneficiarioRepository):
    def busca_por_id(self, id: 'UUID') -> 'Beneficiario':
        return BeneficiarioFactory.build()


class ContaRepositoryMock(ContaRepository):
    def lista_por_ids(self, ids: List['UUID']) -> List['UUID']:
        return ContaFactory.build_batch(10)


class PromisoriaRepositoryMock(PromisoriaRepository):
    def insere(self, promisoria: 'Promisoria'):
        ...
