from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from dashboard.views import DashboardView


class TestDashboardView(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create(username='flaviogf')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_dashboard_view_get(self):
        url = ''

        client = Client()

        client.login(username='flaviogf', password='teste123!')

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)
