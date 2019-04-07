import unittest
import uuid
from datetime import datetime
from json import dumps
from unittest.mock import Mock

from common.domain.events import EventPublisher, StoredEvent


class EventPublisherTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.sut = EventPublisher.instancia()

    def tearDown(self) -> 'None':
        self.sut.reset()

    def test_subscribe(self) -> 'None':
        self.sut.subscribe(lambda x: print('OK'))

        self.assertEqual(1, len(self.sut.subscribers))

    def test_publish(self) -> 'None':
        subscriber = Mock()

        event = 'Teste'

        self.sut.subscribe(subscriber)

        self.sut.publish(event)

        subscriber.assert_called_with(event)


class StoredEventTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.evento = {'nome': 'flavio'}
        self.json = dumps(self.evento)

        self.sut = StoredEvent(str(type(self.evento)), self.json)

    def test_init(self) -> 'None':
        self.assertIsInstance(self.sut.id, uuid.UUID)
        self.assertIsInstance(self.sut.type, str)
        self.assertEqual(self.json, self.sut.json)
        self.assertIsInstance(self.sut.data, datetime)
