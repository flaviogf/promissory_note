from domain.core.commands import SolicitarPromissoriaCommand
from domain.core.events import PromissoriaEmitidaEvent
from domain.core.repositories import EmitenteRepository, BeneficiarioRepository, PromissoriaRepository
from domain.core.services import EmailService
from domain.shared.handlers import Handler


class SolicitarPromissoriaHandler(Handler):

    def __init__(self,
                 emitente_repository: 'EmitenteRepository',
                 beneficiario_repository: 'BeneficiarioRepository',
                 promissoria_repository: 'PromissoriaRepository',
                 promissoria_emitida_handler: 'PromissoriaEmitidaHandler'):
        super().__init__()
        self.emitente_repository = emitente_repository
        self.beneficiario_repository = beneficiario_repository
        self.promissoria_repository = promissoria_repository
        self.promissoria_emitida_handler = promissoria_emitida_handler

    def handle(self, command: 'SolicitarPromissoriaCommand'):
        emitente = self.emitente_repository.busca_por_id(command.id_emitente)

        beneficiario = self.beneficiario_repository.busca_por_id(command.id_beneficiario)

        promissoria = emitente.emite_promissoria(numero=command.numero,
                                                 data_vencimento=command.data_vencimento,
                                                 valor=command.valor,
                                                 beneficiario=beneficiario)

        promissoria_emitida = PromissoriaEmitidaEvent(numero=promissoria.numero,
                                                      data_vencimento=promissoria.data_vencimento,
                                                      valor=promissoria.valor,
                                                      nome_beneficiario=promissoria.beneficiario.nome,
                                                      documento_beneficiario=promissoria.beneficiario.documento,
                                                      email_beneficiario=promissoria.beneficiario.email,
                                                      nome_emitente=promissoria.emitente.nome,
                                                      documento_emitente=promissoria.emitente.documento,
                                                      email_emitente=promissoria.emitente.email,
                                                      endereco_emitente=promissoria.emitente.endereco,
                                                      data_emissao=promissoria.data_emissao,
                                                      recebida=promissoria.recebida)

        self.promissoria_repository.insere(promissoria)

        self.promissoria_emitida_handler.send(promissoria_emitida)


class PromissoriaEmitidaHandler(Handler):

    def __init__(self, email_service: 'EmailService'):
        self.email_service = email_service

    def send(self, event: 'PromissoriaEmitidaEvent'):
        self.email_service.envia(event.email_beneficiario, 'Uma promissoria foi emitida para você')
        self.email_service.envia(event.email_emitente, 'Uma promissoria foi emitida em seu nome')
