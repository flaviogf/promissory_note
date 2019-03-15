from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


class ContaViewSetTests(APITestCase):
    def test_conta_view_set_list(self):
        url = reverse('conta-list')

        response = self.client.get(url)

        self.assertEqual(HTTP_200_OK, response.status_code)
