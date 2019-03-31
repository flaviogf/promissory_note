from datetime import datetime

from domain.shared.entities import Entity


class Promissoria(Entity):
    def __init__(self, numero, data_vencimento, valor, beneficiario, emitente):
        super().__init__()
        self.numero = numero
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.beneficiario = beneficiario
        self.emitente = emitente
        self.data_emissao = datetime.now()
        self.recebida = False


class Emitente(Entity):
    def __init__(self, nome, documento, endereco, email):
        super().__init__()
        self.nome = nome
        self.documento = documento
        self.endereco = endereco
        self.email = email
