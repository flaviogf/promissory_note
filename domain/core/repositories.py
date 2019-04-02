from abc import ABC

from domain.core.entities import Promissoria
from domain.shared.repositories import Repository


class EmitenteRepository(Repository, ABC):
    def busca_por_id(self, id):
        raise NotImplementedError()


class BeneficiarioRepository(Repository, ABC):
    def busca_por_id(self, id):
        raise NotImplementedError()


class PromissoriaRepository(Repository, ABC):
    def insere(self, promissoria: 'Promissoria'):
        raise NotImplementedError()
