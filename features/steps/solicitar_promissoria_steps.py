import uuid
from datetime import datetime
from unittest import mock

from behave import given, when, then

from domain.core.commands import SolicitarPromissoriaCommand
from domain.core.handlers import SolicitarPromissoriaHandler


@given('um numero')
def step_impl(context):
    context.numero = '123'


@given('uma data de vencimento')
def step_impl(context):
    context.data_vencimento = datetime.now()


@given('um valor')
def step_impl(context):
    context.valor = 10


@given('um beneficiario')
def step_impl(context):
    context.id_beneficiario = uuid.uuid4()


@given('um emitente')
def step_impl(context):
    context.id_emitente = uuid.uuid4()


@when('solicitado uma promissoria')
def step_impl(context):
    context.command = SolicitarPromissoriaCommand(numero=context.numero,
                                                  data_vencimento=context.data_vencimento,
                                                  valor=context.valor,
                                                  id_beneficiario=context.id_beneficiario,
                                                  id_emitente=context.id_emitente)


@then('uma promissoria deve ser emitida')
def step_impl(context):
    with mock.patch('domain.core.repositories.EmitenteRepository') as emitente_repository, \
        mock.patch('domain.core.repositories.BeneficiarioRepository') as beneficiario_repository, \
        mock.patch('domain.core.repositories.PromissoriaRepository') as promissoria_repository, \
        mock.patch('domain.core.handlers.PromissoriaEmitidaHandler') as promissoria_emitida_handler:
        handler = SolicitarPromissoriaHandler(emitente_repository=emitente_repository,
                                              beneficiario_repository=beneficiario_repository,
                                              promissoria_repository=promissoria_repository,
                                              promissoria_emitida_handler=promissoria_emitida_handler)
        handler.handle(context.command)

        emitente_repository.busca_por_id.assert_called_with(context.command.id_emitente)
        beneficiario_repository.busca_por_id.assert_called_with(context.command.id_beneficiario)
        promissoria_repository.insere.assert_called_once()
