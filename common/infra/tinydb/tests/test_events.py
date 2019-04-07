import os
import unittest

from common.domain.events import Event
from common.infra.tinydb.events import TinyDBEventStore


class TinyDBEventStoreTests(unittest.TestCase):
    def setUp(self) -> 'None':
        self.path = 'event_store_tests.json'

        self.sut = TinyDBEventStore(self.path)

    def tearDown(self) -> 'None':
        os.remove(self.path)

    def test_salva(self) -> 'None':
        class EventoFake(Event):
            ...

        evento = EventoFake()

        self.sut.salva(evento)
