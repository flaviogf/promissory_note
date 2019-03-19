import factory
from django.test import TestCase

from contas.models import Conta
from contatos.models import Contato
from core.models import Promisoria
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


class PromisoriaTests(TestCase):
    def setUp(self):
        self.contato1 = ContatoFactory.create()
        self.endereco1 = EnderecoFactory.create()
        self.conta1 = ContaFactory.create()

        self.sut = Promisoria.objects.create(
            contato=self.contato1, endereco=self.endereco1)
        self.sut.contas.add(self.conta1)

    def test_promisoria_create(self):
        self.assertEqual(self.contato1, self.sut.contato)
        self.assertEqual(self.endereco1, self.sut.endereco)
        self.assertEqual(1, self.sut.contas.count())
