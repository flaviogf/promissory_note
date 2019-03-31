from abc import ABC


class Repository(ABC):
    def busca_por_id(self, id):
        raise NotImplementedError()
