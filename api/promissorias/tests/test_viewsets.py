import uuid

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIRequestFactory

from api.promissorias.viewsets import PromissoriaViewSet


class SolicitarPromissoriaViewSetTests(TestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.url = reverse('promissorias-list')
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
        self.sut = PromissoriaViewSet

    def test_post_ok(self):
        view = self.sut.as_view({'post': 'create'})
        request = self.request_factory.post(self.url, data=self.data)
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_post_bad_request(self):
        view = self.sut.as_view({'post': 'create'})
        request = self.request_factory.post(self.url, data={})
        response = view(request)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)
