from domain.core.entities import Promissoria
from domain.shared.repositories import Repository


class EmitenteRepository(Repository):
    ...


class BeneficiarioRepository(Repository):
    ...


class PromissoriaRepository(Repository):
    def insere(self, promissoria: 'Promissoria'):
        raise NotImplementedError()
