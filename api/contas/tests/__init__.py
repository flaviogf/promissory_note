import factory
from faker import Faker

from api.contas.models import ContaModel

fake = Faker('pt_BR')


class ContaModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContaModel

    descricao = fake.sentence()
    valor = 1000.00
