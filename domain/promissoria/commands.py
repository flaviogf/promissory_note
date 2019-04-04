import uuid
from datetime import datetime

from domain.shared.commands import Comand


class SolicitarPromissoriaCommand(Comand):
    def __init__(self,
                 numero: 'str',
                 data_vencimento: 'datetime',
                 valor: 'float',
                 id_beneficiario: 'uuid.UUID',
                 id_emitente: 'uuid.UUID'):
        super().__init__()
        self.numero = numero
        self.data_vencimento = data_vencimento
        self.valor = valor
        self.id_beneficiario = id_beneficiario
        self.id_emitente = id_emitente
