import uuid
from json import JSONEncoder


class Encoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, uuid.UUID):
            return o.__str__()

        return super().default(o)
