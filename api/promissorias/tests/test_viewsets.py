from unittest import mock

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIRequestFactory

from api.beneficiarios.models import Beneficiario
from api.emitentes.models import Emitente
from api.promissorias.viewsets import PromissoriaViewSet


class SolicitarPromissoriaViewSetTests(TestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.url = reverse('promissorias-list')
        self.numero = '1'
        self.data_vencimento = timezone.now()
        self.valor = 50

        self.beneficiario = Beneficiario.objects.create(nome='Bruce',
                                                        documento='123',
                                                        email='batman@email.com')

        self.emitente = Emitente.objects.create(nome='Bruce',
                                                documento='123',
                                                email='batman@email.com',
                                                endereco='gotham')

        self.data = {
            'numero': self.numero,
            'data_vencimento': self.data_vencimento,
            'valor': self.valor,
            'id_beneficiario': self.beneficiario.id,
            'id_emitente': self.emitente.id,
        }
        self.sut = PromissoriaViewSet

    @mock.patch("infra.ioc.get_solicitar_promissoria_handler")
    def test_post_ok(self, _):
        view = self.sut.as_view({'post': 'create'})
        request = self.request_factory.post(self.url, data=self.data)
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)

    @mock.patch("infra.ioc.get_solicitar_promissoria_handler")
    def test_post_bad_request(self, _):
        view = self.sut.as_view({'post': 'create'})
        request = self.request_factory.post(self.url, data={})
        response = view(request)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)
