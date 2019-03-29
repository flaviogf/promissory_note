from typing import List

from shared.repositories import Repository


class EmitenteRepository(Repository):
    def busca_por_id(self, id: 'UUID') -> 'Emitente':
        raise NotImplementedError()


class BeneficiarioRepository(Repository):
    def busca_por_id(self, id: 'UUID') -> 'Beneficiario':
        raise NotImplementedError()


class ContaRepository(Repository):
    def lista_por_id(self, ids: List['UUID']) -> List['Conta']:
        raise NotImplementedError()


class PromisoriaRepository(Repository):
    def insere(self, promisoria: 'Promisoria'):
        raise NotImplementedError()
