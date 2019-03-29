"""modulo dos handlers do shared"""


class Handler:
    """classe base para os handlers"""

    def handle(self, *args, **kwargs):
        raise NotImplementedError()
