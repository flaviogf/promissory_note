from datetime import datetime

from shared.entities import Entity


class Conta(Entity):
    def __init__(self, descricao: str, valor: float):
        super().__init__()
        self._descricao = descricao
        self._valor = valor
        self._data_recebimento = None
        self._recebida = False

    def __add__(self, conta):
        return self.valor + conta.valor

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def data_recebimento(self) -> datetime:
        return self._data_recebimento

    @property
    def recebida(self) -> bool:
        return self._recebida

    def recebe(self):
        self._recebida = True
        self._data_recebimento = datetime.now()


class Promisoria(Entity):
    def __init__(self, emitente: 'Emitente', beneficiario: 'Beneficiario'):
        super().__init__()
        self._emitente = emitente
        self._beneficiario = beneficiario
        self._contas = []

    def __iadd__(self, conta):
        self.adiciona_conta(conta)
        return self

    @property
    def emitente(self):
        return self._emitente

    @property
    def beneficiario(self):
        return self._beneficiario

    @property
    def contas(self):
        return [*self._contas]

    @property
    def total(self):
        return sum([it.valor for it in self.contas])

    def adiciona_conta(self, conta: 'Conta'):
        self._contas.append(conta)

    def recebe(self):
        for it in self.contas:
            it.recebe()


class Pessoa(Entity):
    def __init__(self, nome: str, endereco: str, telefone: str):
        super().__init__()
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def telefone(self) -> str:
        return self._telefone


class Emitente(Pessoa):
    ...


class Beneficiario(Pessoa):
    ...
