from domain.core.commands import SolicitarPromissoriaCommand
from domain.core.repositories import EmitenteRepository, BeneficiarioRepository, PromissoriaRepository
from domain.shared.handlers import Handler


class SolicitarPromissoriaHandler(Handler):
    def __init__(self,
                 emitente_repository: 'EmitenteRepository',
                 beneficiario_repository: 'BeneficiarioRepository',
                 promissoria_repository: 'PromissoriaRepository'):
        super().__init__()
        self.emitente_repository = emitente_repository
        self.beneficiario_repository = beneficiario_repository
        self.promissoria_repository = promissoria_repository

    def handle(self, command: 'SolicitarPromissoriaCommand'):
        emitente = self.emitente_repository.busca_por_id(command.id_emitente)

        beneficiario = self.beneficiario_repository.busca_por_id(command.id_beneficiario)

        promissoria = emitente.emite_promissoria(numero=command.numero,
                                                 data_vencimento=command.data_vencimento,
                                                 valor=command.valor,
                                                 beneficiario=beneficiario)

        self.promissoria_repository.insere(promissoria)
