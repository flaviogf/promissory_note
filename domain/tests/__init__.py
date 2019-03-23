import factory
from faker import Faker

from domain.entities import Beneficiario, Conta, Emitente, Promisoria

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
