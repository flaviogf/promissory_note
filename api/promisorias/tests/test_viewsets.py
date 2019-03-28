from django.test import TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIRequestFactory

from api.promisorias.viewsets import PromisoriaViewSet


class PromisoriaViewSetTests(TestCase):
    def setUp(self):
        self.request_factory = APIRequestFactory()
        self.url = reverse('promisoria-list')
        self.sut = PromisoriaViewSet

    def test_list(self):
        view = self.sut.as_view({'get': 'list'})
        request = self.request_factory.get(self.url)
        response = view(request)
        self.assertEqual(HTTP_200_OK, response.status_code)
