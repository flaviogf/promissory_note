"""modulo das entidades do shared"""


import uuid


class Entity:
    """classe base para as entidades"""

    def __init__(self):
        self.id = uuid.uuid4()
