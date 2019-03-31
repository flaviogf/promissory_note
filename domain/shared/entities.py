import uuid
from abc import ABC


class Entity(ABC):
    def __init__(self):
        self.id = uuid.uuid4()
