from api.beneficiarios.repositories import DjangoBeneficiarioRepository
from api.emitentes.repositories import DjangoEmitenteRepository
from api.promissorias.repositories import DjangoPromissoriaRepository
from domain.core.handlers import SolicitarPromissoriaHandler, PromissoriaEmitidaHandler
from domain.core.repositories import BeneficiarioRepository, EmitenteRepository, PromissoriaRepository
from domain.core.services import EmailService
from infra.services import RabbitEmailService


def get_beneficiario_repository() -> 'BeneficiarioRepository':
    return DjangoBeneficiarioRepository()


def get_emitente_repository() -> 'EmitenteRepository':
    return DjangoEmitenteRepository()


def get_promissoria_repository() -> 'PromissoriaRepository':
    return DjangoPromissoriaRepository()


def get_solicitar_promissoria_handler() -> 'SolicitarPromissoriaHandler':
    return SolicitarPromissoriaHandler(emitente_repository=get_emitente_repository(),
                                       beneficiario_repository=get_beneficiario_repository(),
                                       promissoria_repository=get_promissoria_repository(),
                                       promissoria_emitida_handler=get_promissoria_emitida_handler())


def get_email_service() -> 'EmailService':
    return RabbitEmailService()


def get_promissoria_emitida_handler() -> 'PromissoriaEmitidaHandler':
    return PromissoriaEmitidaHandler(email_service=get_email_service())
