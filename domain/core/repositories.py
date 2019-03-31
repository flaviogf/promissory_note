from abc import ABC

from domain.core.entities import Promissoria
from domain.shared.repositories import Repository


class EmitenteRepository(Repository, ABC):
    ...


class BeneficiarioRepository(Repository, ABC):
    ...


class PromissoriaRepository(Repository, ABC):
    def insere(self, promissoria: 'Promissoria'):
        raise NotImplementedError()
