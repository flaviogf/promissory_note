from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


class PromisoriaViewSetTests(APITestCase):
    def setUp(self):
        self.url = reverse('promisoria-list')

    def test_promisoria_viewset_list(self):
        response = self.client.get(self.url)
        self.assertEqual(HTTP_200_OK, response.status_code)
