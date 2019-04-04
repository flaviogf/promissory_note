import os
from typing import Callable

import pika

from api.beneficiarios.repositories import DjangoBeneficiarioRepository
from api.emitentes.repositories import DjangoEmitenteRepository
from api.promissorias.repositories import DjangoPromissoriaRepository
from domain.promissoria.handlers import SolicitarPromissoriaHandler, PromissoriaEmitidaHandler
from domain.promissoria.repositories import BeneficiarioRepository, EmitenteRepository, PromissoriaRepository
from domain.promissoria.services import EmailService
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


def get_rabbit_connection() -> 'Callable':
    def func():
        return pika.BlockingConnection(pika.ConnectionParameters(os.getenv('URL_RABBIT', 'localhost')))

    return func


def get_email_service() -> 'EmailService':
    return RabbitEmailService(get_rabbit_connection=get_rabbit_connection())


def get_promissoria_emitida_handler() -> 'PromissoriaEmitidaHandler':
    return PromissoriaEmitidaHandler(email_service=get_email_service())
