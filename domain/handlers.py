"""modulo dos handlers do dominio"""


from domain.commands import EmitirPromisoriaCommandResult
from shared.handlers import Handler


class EmitirPromisoriaHandler(Handler):
    """classe responsavel pelo fluxo de criação de uma promisória"""

    def __init__(self,
                 emitente_repository: 'EmitenteRepository',
                 beneficiario_repository: 'BeneficiarioRepository',
                 conta_repository: 'ContaRepository',
                 promisoria_repository: 'PromisoriaRepository'):
        self.emitente_repository = emitente_repository
        self.beneficiario_repository = beneficiario_repository
        self.conta_repository = conta_repository
        self.promisoria_repository = promisoria_repository

    def handle(self, command: 'EmitirPromisoriaCommand') -> 'EmitirPromisoriaCommandResult':
        """realiza o fluxo de criação de uma promisória"""
        emitente = self.emitente_repository.busca_por_id(command.id_emitente)

        contas = self.conta_repository.lista_por_id(command.id_contas)

        promisoria = emitente.emite_promisoria()

        for it in contas:
            promisoria += it

        self.promisoria_repository.insere(promisoria)

        return EmitirPromisoriaCommandResult(mensagem='promisória criada com sucesso')
