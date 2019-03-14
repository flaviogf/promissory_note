from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


class EnderecoViewSetTests(APITestCase):
    def test_endereco_view_set_list(self):
        url = reverse('endereco-list')

        response = self.client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)
