import os
import uuid
from json import dumps, JSONEncoder
from typing import Optional

from tinydb import TinyDB

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
        class UUIDEnconder(JSONEncoder):

            def default(self, o):
                if isinstance(o, uuid.UUID):
                    return o.__str__()

                return super().default(o)

        stored_event = StoredEvent(str(type(event)),
                                   dumps(event.__dict__, cls=UUIDEnconder))

        with TinyDB(self.path) as db:
            db.insert({
                'id': stored_event.id.__str__(),
                'type': stored_event.type,
                'json': stored_event.json,
                'data': stored_event.data.strftime('%d/%m/%y %H:%M:%S')
            })
