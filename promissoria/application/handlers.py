from common.application.decorators import event_store, event_publisher
from common.application.handlers import Handler

from promissoria.application.commands import CadastrarEmitenteCommand, CadastrarBeneficiarioCommand
from promissoria.domain.entities import Emitente
from promissoria.domain.repositories import EmitenteRepository


class CadastrarEmitente(Handler):
    def __init__(self, emitente_repository: 'EmitenteRepository'):
        self.emitente_repository = emitente_repository

    @event_publisher
    @event_store
    def handle(self, command: 'CadastrarEmitenteCommand') -> 'None':
        emitente = Emitente(nome=command.nome,
                            cpf=command.cpf,
                            endereco=command.endereco)

        self.emitente_repository.salva(emitente)


class CadastrarBeneficiarioHandler(Handler):

    @event_publisher
    @event_store
    def handle(self, command: 'CadastrarBeneficiarioCommand') -> 'None':
        pass
