from common.domain.events import EventPublisher
from common.infra.tinydb.events import TinyDBEventStore


class ApplicationLifeCycle:
    event_store = TinyDBEventStore.instancia()

    @classmethod
    def listen(cls, func):
        def wrapper(*args, **kwargs):
            EventPublisher.instancia().subscribe(cls.event_store.salva)

            func(*args, **kwargs)

        return wrapper
