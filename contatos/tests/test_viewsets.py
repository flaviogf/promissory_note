from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


class ContatoViewSetTests(APITestCase):
    def test_contato_view_set_list(self):
        url = reverse('contato-list')

        response = self.client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)
