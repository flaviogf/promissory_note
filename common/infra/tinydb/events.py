import os
from json import dumps
from typing import Optional

from tinydb import TinyDB

from common.application.enconders import Encoder
from common.domain.events import EventStore, Event, StoredEvent


class TinyDBEventStore(EventStore):
    def __init__(self, path: 'Optional[str]' = None):
        self.path = path or os.path.join(os.getenv('HOME'), 'event_store_db.json')

    @classmethod
    def instancia(cls):
        if not hasattr(cls, '_instancia'):
            cls._instancia = TinyDBEventStore()

        return cls._instancia

    def salva(self, event: 'Event') -> 'None':
        stored_event = StoredEvent(str(type(event)), dumps(event.__dict__, cls=Encoder))

        with TinyDB(self.path) as db:
            db.insert({
                'id': stored_event.id.__str__(),
                'type': stored_event.type,
                'json': stored_event.json,
                'data': stored_event.data.strftime('%d/%m/%y %H:%M:%S')
            })
