from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIRequestFactory

from api.beneficiarios.tests import BeneficiarioModelFactory
from api.contas.tests import ContaModelFactory
from api.emitentes.tests import EmitenteModelFactory
from api.promisorias.viewsets import PromisoriaViewSet


class PromisoriaViewSetTests(TestCase):
    def setUp(self):
        self.beneficiario = BeneficiarioModelFactory.create()
        self.emitente = EmitenteModelFactory.create()
        self.conta = ContaModelFactory.create()
        self.request_factory = APIRequestFactory()
        self.url = reverse('promisoria-list')
        self.url_emite_promisoria = reverse('promisoria-emite')
        self.sut = PromisoriaViewSet

    def test_list(self):
        view = self.sut.as_view({'get': 'list'})
        request = self.request_factory.get(self.url)
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_emite_promisoria(self):
        view = self.sut.as_view({'post': 'emite_promisoria'})
        data = {
            'emitente': self.emitente.id,
            'beneficiario': self.beneficiario.id,
            'contas': [self.conta.id]
        }
        request = self.request_factory.post(self.url_emite_promisoria, data, format='json')
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual('promisória criada com sucesso', response.data)
