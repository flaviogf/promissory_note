import uuid
from datetime import datetime


class Promissoria:
    def __init__(self, numero, data_vencimento, valor, beneficiario, emitente):
        self.id = uuid.uuid4()
        self.numero = numero
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.beneficiario = beneficiario
        self.emitente = emitente
        self.data_emissao = datetime.now()
        self.recebida = False
