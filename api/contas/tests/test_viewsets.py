"""modulo de testes dos viewsets do app contas"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIRequestFactory

from api.contas.viewsets import ContaViewSet


class ContaViewSetTests(TestCase):
    """classe responsavel pelos testes da classe ContaViewSet"""
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.url = reverse('conta-list')
        self.sut = ContaViewSet

    def test_list(self):
        """testa o metodo list"""
        view = self.sut.as_view({'get': 'list'})
        request = self.request_factory.get(self.url)
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)
