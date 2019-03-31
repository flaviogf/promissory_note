import uuid

from django.test import TestCase
from django.utils import timezone

from api.promissorias.serializers import SolicitarPromissoriaSerializer


class SolicitarPromissoriaSerializerTests(TestCase):
    def setUp(self):
        self.numero = '1'
        self.data_vencimento = timezone.now()
        self.valor = 50
        self.id_beneficiario = uuid.uuid4()
        self.id_emitente = uuid.uuid4()
        self.data = {
            'numero': self.numero,
            'data_vencimento': self.data_vencimento,
            'valor': self.valor,
            'id_beneficiario': self.id_beneficiario,
            'id_emitente': self.id_emitente,
        }
        self.sut = SolicitarPromissoriaSerializer(data=self.data)

    def test_is_valid(self):
        self.assertTrue(self.sut.is_valid())
