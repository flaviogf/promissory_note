from domain.core.entities import Promissoria
from domain.core.repositories import PromissoriaRepository


class DjangoPromissoriaRepository(PromissoriaRepository):
    def insere(self, promissoria: 'Promissoria'):
        # TODO implementar
        raise NotImplementedError()
