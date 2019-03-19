import factory

from contas.models import Conta
from contatos.models import Contato
from enderecos.models import Endereco


class ContatoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contato

    nome = factory.Faker('name')
    email = factory.Faker('email')
    telefone = factory.Faker('phone_number')


class EnderecoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Endereco

    cep = factory.Faker('postcode')
    rua = factory.Faker('street_address')
    bairro = factory.Faker('bairro', locale='pt_BR')
    numero = factory.Faker('building_number')


class ContaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Conta

    descricao = factory.Faker('sentence')
    valor = 1000.00
    data_recebimento = factory.Faker('future_datetime', end_date='+30d')
    recebida = factory.Faker('pybool')
