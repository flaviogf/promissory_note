from common.domain.events import EventPublisher
from common.infra.tinydb.events import TinyDBEventStore


def event_publisher(func):
    def wrapper(*args, **kwargs):
        EventPublisher.instancia().reset()

        result = func(*args, **kwargs)

        EventPublisher.instancia().reset()
        return result

    return wrapper


def event_store(func):
    def wrapper(*args, **kwargs):
        db = TinyDBEventStore.instancia()

        EventPublisher.instancia().subscribe(db.salva)

        return func(*args, **kwargs)

    return wrapper
