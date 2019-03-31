from datetime import datetime

from domain.shared.events import Event


class PromissoriaEmitidaEvent(Event):
    def __init__(self,
                 numero: 'str',
                 data_vencimento: 'datetime',
                 valor: 'float',
                 nome_beneficiario: 'str',
                 documento_beneficiario: 'str',
                 email_beneficiario: 'str',
                 nome_emitente: 'str',
                 documento_emitente: 'str',
                 email_emitente: 'str',
                 endereco_emitente: 'str',
                 data_emissao: 'datetime',
                 recebida: 'bool'):
        super().__init__()
        self.numero = numero
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.nome_beneficiario = nome_beneficiario
        self.documento_beneficiario = documento_beneficiario
        self.email_beneficiario = email_beneficiario
        self.nome_emitente = nome_emitente
        self.documento_emitente = documento_emitente
        self.email_emitente = email_emitente
        self.endereco_emitente = endereco_emitente
        self.data_emissao = data_emissao
        self.recebida = recebida
