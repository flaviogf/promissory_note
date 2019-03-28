from api.beneficiarios.repositories import DjangoBeneficiarioRepository
from api.contas.repositories import DjangoContaRepository
from api.emitentes.repositories import DjangoEmitenteRepository
from api.promisorias.repositories import DjangoPromisoriaRepository
from domain.handlers import EmitirPromisoriaHandler


def get_emitente_repository():
    return DjangoEmitenteRepository()


def get_beneficiario_repository():
    return DjangoBeneficiarioRepository()


def get_conta_repository():
    return DjangoContaRepository()


def get_promisoria_repository():
    return DjangoPromisoriaRepository()


def get_emitir_promisoria_handler():
    return EmitirPromisoriaHandler(emitente_repository=get_emitente_repository(),
                                   beneficiario_repository=get_emitente_repository(),
                                   conta_repository=get_conta_repository(),
                                   promisoria_repository=get_promisoria_repository())
