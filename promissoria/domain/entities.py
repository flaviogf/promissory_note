from common.domain.entities import Entity
from common.domain.events import EventPublisher
from promissoria.domain.events import EmitenteCadastrado


class Emitente(Entity):
    def __init__(self, nome: 'str', cpf: 'str', endereco: 'str'):
        super().__init__()
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

        EventPublisher.instancia().publish(EmitenteCadastrado(nome=nome,
                                                              cpf=cpf,
                                                              endereco=endereco))

    @property
    def nome(self) -> 'str':
        return self._nome

    @property
    def cpf(self) -> 'str':
        return self._cpf

    @property
    def endereco(self) -> 'str':
        return self._endereco
