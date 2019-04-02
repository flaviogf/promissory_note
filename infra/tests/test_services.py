import unittest
from unittest import mock

from infra.services import RabbitEmailService


class RabbitEmailServiceTests(unittest.TestCase):

    @mock.patch('pika.BlockingConnection')
    def setUp(self, rabbit_connection):
        self.rabbit_connection = rabbit_connection

        self.sut = RabbitEmailService(get_rabbit_connection=lambda: self.rabbit_connection)

    def test_envia(self):
        self.sut.envia('clark', 'nd...')

        self.rabbit_connection.channel.assert_called_once()
