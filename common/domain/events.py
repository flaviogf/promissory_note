import uuid
from abc import ABC
from datetime import datetime
from typing import List, Callable, Optional


class EventPublisher:
    def __init__(self):
        self._subscribers = []

    @classmethod
    def instancia(cls) -> 'EventPublisher':
        if not hasattr(cls, '_instancia'):
            cls._instancia = EventPublisher()

        return cls._instancia

    @property
    def subscribers(self) -> 'List[Callable[[Event], None]]':
        return self._subscribers

    def subscribe(self, subscriber: 'Callable[[Event], None]') -> 'None':
        self._subscribers.append(subscriber)

    def publish(self, event: 'Event') -> 'None':
        for it in self._subscribers:
            it(event)

    def reset(self) -> 'None':
        self._subscribers = []


class Event(ABC):
    def __init__(self):
        self.id = uuid.uuid4()


class EventStore(ABC):
    def salva(self, event: 'Event') -> 'None':
        raise NotImplementedError()


class StoredEvent:
    def __init__(self, _type: 'str', json: 'str', data: 'Optional[datetime]' = None):
        self.id = uuid.uuid4()
        self.type = _type
        self.json = json
        self.data = data or datetime.now()
