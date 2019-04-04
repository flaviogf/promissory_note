import uuid
from datetime import datetime

from domain.shared.entities import Entity


class Promissoria(Entity):
    def __init__(self,
                 numero: 'str',
                 data_vencimento: 'datetime',
                 valor: 'float',
                 beneficiario: 'Beneficiario',
                 emitente: 'Emitente'):
        super().__init__()
        self.numero = numero
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.beneficiario = beneficiario
        self.emitente = emitente
        self.data_emissao = datetime.now()
        self.recebida = False


class Pessoa(Entity):
    def __init__(self, nome: 'str', documento: 'str', email: 'str'):
        super().__init__()
        self.nome = nome
        self.documento = documento
        self.email = email


class Emitente(Pessoa):
    def __init__(self, nome: 'str', documento: 'str', email: 'str', endereco: 'str'):
        super().__init__(nome, documento, email)
        self.endereco = endereco

    def emite_promissoria(self,
                          numero: 'str',
                          data_vencimento: 'datetime',
                          valor: 'float',
                          beneficiario: 'Beneficiario') -> 'Promissoria':
        return Promissoria(numero=numero,
                           data_vencimento=data_vencimento,
                           valor=valor,
                           beneficiario=beneficiario,
                           emitente=self)

    class Factory:
        @staticmethod
        def cria(id: 'uuid.UUID', nome: 'str', documento: 'str', email: 'str', endereco: 'str'):
            beneficiario = Emitente(nome, documento, email, endereco)
            beneficiario.id = id
            return beneficiario


class Beneficiario(Pessoa):
    class Factory:
        @staticmethod
        def cria(id: 'uuid.UUID', nome: 'str', documento: 'str', email: 'str'):
            beneficiario = Beneficiario(nome, documento, email)
            beneficiario.id = id
            return beneficiario
