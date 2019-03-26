import factory
from faker import Faker

from api.emitentes.models import EmitenteModel

fake = Faker('pt_br')


class EmitenteModelFactory(factory.django.DjangoModelFactory):
    """classe para a criação de emitente"""
    class Meta:
        model = EmitenteModel

    nome = factory.Faker('name')
    endereco = factory.Faker('address')
    telefone = factory.Faker('phone_number')
