from api.promisorias.models import PromisoriaModel
from domain.repositories import PromisoriaRepository


class DjangoPromisoriaRepository(PromisoriaRepository):
    def insere(self, promisoria):
        ...
