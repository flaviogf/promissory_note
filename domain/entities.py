from datetime import datetime
from typing import List

from shared.entities import Entity


class Conta(Entity):
    def __init__(self, descricao: str, valor: float):
        super().__init__()
        self._descricao = descricao
        self._valor = valor
        self._data_recebimento = None
        self._recebida = False

    def __add__(self, conta: 'Conta'):
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

    class Factory:
        @staticmethod
        def cria(id: 'uuid.UUID',
                 descricao: str,
                 valor: float,
                 data_recebimento: 'datetime',
                 recebida: bool):
            conta = Conta(descricao=descricao, valor=valor)
            conta.id = id
            conta._data_recebimento = data_recebimento
            conta._recebida = recebida
            return conta


class Promisoria(Entity):
    def __init__(self, emitente: 'Emitente'):
        super().__init__()
        self._emitente = emitente
        self._beneficiario = None
        self._contas = []
        self._data_recebimento = None
        self._recebida = False

    def __iadd__(self, conta: 'Conta'):
        self.adiciona_conta(conta)
        return self

    def dict(self):
        return {
            'emitente': self.emitente.id,
            'beneficiario': self.beneficiario.id,
            'contas': [it.id for it in self.contas],
            'data_recebimento': self.data_recebimento,
            'recebida': self.recebida
        }

    @property
    def emitente(self) -> 'Emitente':
        return self._emitente

    @property
    def beneficiario(self) -> 'Beneficiario':
        return self._beneficiario

    @property
    def contas(self) -> List['Conta']:
        return [*self._contas]

    @property
    def total(self) -> float:
        return sum([it.valor for it in self.contas])

    @property
    def data_recebimento(self) -> datetime:
        return self._data_recebimento

    @property
    def recebida(self) -> bool:
        return self._recebida

    def adiciona_conta(self, conta: 'Conta'):
        self._contas.append(conta)

    def recebe(self, beneficiario: 'Beneficiario'):
        for it in self.contas:
            it.recebe()

        self._beneficiario = beneficiario
        self._data_recebimento = datetime.now()
        self._recebida = True


class Pessoa(Entity):
    def __init__(self, nome: str, endereco: str, telefone: str):
        super().__init__()
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    def dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone
        }

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
    def emite_promisoria(self) -> 'Promisoria':
        return Promisoria(emitente=self)

    class Factory:
        @staticmethod
        def cria(id: 'uuid.UUID', nome: str, endereco: str, telefone: str):
            emitente = Emitente(nome, endereco, telefone)
            emitente.id = id
            return emitente


class Beneficiario(Pessoa):
    def __init__(self, nome: str, endereco: str, telefone: str):
        super().__init__(nome, endereco, telefone)
        self._promissorias_recebidas = []

    @property
    def promisorias_recebidas(self) -> List['Promisoria']:
        return [*self._promissorias_recebidas]

    def recebe(self, promisoria: 'Promisoria'):
        promisoria.recebe(self)
        self._adiciona_promisoria(promisoria)

    def _adiciona_promisoria(self, promisoria: 'Promisoria'):
        self._promissorias_recebidas.append(promisoria)

    class Factory:
        @staticmethod
        def cria(id: 'uuid.UUID', nome: str, endereco: str, telefone: str):
            beneficiario = Beneficiario(nome, endereco, telefone)
            beneficiario.id = id
            return beneficiario
