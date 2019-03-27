import factory
from faker import Faker

from api.beneficiarios.models import BeneficiarioModel

fake = Faker('pt_BR')


class BeneficiarioModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BeneficiarioModel

    nome = factory.Faker('name')
    endereco = factory.Faker('address')
    telefone = factory.Faker('phone_number')
