from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import Client, TestCase

from dashboard.views import DashboardView


class TestDashboardView(TestCase):
    def setUp(self):
        self.usuario = User.objects.create(username='flaviogf')
        self.usuario.set_password('teste123!')
        self.usuario.save()

    def test_dashboard_view_get(self):
        url = ''

        client = Client()

        client.login(username='flaviogf', password='teste123!')

        response = client.get(url)

        self.assertEqual(HTTPStatus.OK, response.status_code)
