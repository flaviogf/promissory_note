from common.domain.repository import Repository
from promissoria.domain.entities import Emitente


class EmitenteRepository(Repository):
    def salva(self, emitente: 'Emitente') -> 'None':
        raise NotImplementedError()
