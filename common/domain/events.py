import uuid
from abc import ABC
from typing import List, Callable


class Event(ABC):
    def __init__(self):
        self.id = uuid.uuid4()


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


class StoredEvent:
    def __init__(self, atype: 'type', data: 'str'):
        self.id = uuid.uuid4()
        self.type = atype
        self.data = data
