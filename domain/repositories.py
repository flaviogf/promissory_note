"""modulo dos repositorios do dominio"""


from typing import List

from shared.repositories import Repository


class EmitenteRepository(Repository):
    """interface para o repositorio de emitente"""

    def busca_por_id(self, id: 'UUID') -> 'Emitente':
        """busca um emitente por id"""
        raise NotImplementedError()


class BeneficiarioRepository(Repository):
    """interface para o repositorios de beneficiario"""

    def busca_por_id(self, id: 'UUID') -> 'Beneficiario':
        """busca um beneficiario por id"""
        raise NotImplementedError()


class ContaRepository(Repository):
    """interface para o repositorio de contas"""

    def lista_por_id(self, ids: List['UUID']) -> List['Conta']:
        """lista contas por ids"""
        raise NotImplementedError()


class PromisoriaRepository(Repository):
    """interface para o repositorio de promisoria"""

    def insere(self, promisoria: 'Promisoria'):
        """insere um promisoria"""
        raise NotImplementedError()
