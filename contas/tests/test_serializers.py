from datetime import datetime

from django.test import TestCase

from contas.serializers import ContaSerializer
from contatos.models import Contato


class TestContaSerializer(TestCase):
    def test_conta_serializer_is_valid_true(self):
        contato = Contato.objects.create(
            nome="Flavio", email="flavio@email.com", telefone="016999999999"
        )

        request = {
            "contato": contato.contato_id,
            "valor": 100.0,
            "data_recebimento_esperado": datetime.now().date(),
        }

        serializer = ContaSerializer(data=request)

        self.assertTrue(serializer.is_valid())
