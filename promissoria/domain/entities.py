from common.domain.entities import Entity
from common.domain.events import EventPublisher
from promissoria.domain.events import EmitenteCadastrado


class Pessoa(Entity):
    def __init__(self, nome: 'str', cpf: 'str'):
        super().__init__()
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self) -> 'str':
        return self._nome

    @property
    def cpf(self) -> 'str':
        return self._cpf


class Emitente(Pessoa):
    def __init__(self, nome: 'str', cpf: 'str', endereco: 'str'):
        super().__init__(nome, cpf)
        self._endereco = endereco

    @property
    def endereco(self) -> 'str':
        return self._endereco

    @staticmethod
    def novo(nome: 'str', cpf: 'str', endereco: 'str') -> 'Emitente':
        emitente = Emitente(nome=nome,
                            cpf=cpf,
                            endereco=endereco)

        EventPublisher.instancia().publish(EmitenteCadastrado(nome=nome,
                                                              cpf=cpf,
                                                              endereco=endereco))

        return emitente


class Beneficiario(Pessoa):
    @staticmethod
    def novo(nome: 'str', cpf: 'str') -> 'Beneficiario':
        beneficiario = Beneficiario(nome=nome,
                                    cpf=cpf)

        return beneficiario
