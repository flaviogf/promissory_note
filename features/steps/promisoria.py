from datetime import datetime

from behave import given, then, when

from domain.entities import Beneficiario, Emitente, Promisoria


@given('uma promisoria')
def step_impl(context):
    emitente = Emitente(nome='Flavio',
                        telefone='01699999999',
                        endereco='Rua x')
    context.promisoria = Promisoria(emitente=emitente)


@when('informado o beneficiario da promisoria')
def step_impl(context):
    context.beneficiario = Beneficiario(nome='Fernando',
                                        telefone='01699999999',
                                        endereco='Rua y')


@when('solicitado o recebimento da promisoria')
def step_impl(context):
    context.promisoria.recebe(context.beneficiario)


@then('a promisoria deve estar marcada como recebida')
def step_impl(context):
    assert context.promisoria.recebida == True


@then('a promisoria deve ter uma data de recebimento')
def step_impl(context):
    assert type(context.promisoria.data_recebimento) == datetime


@then('a promisoria deve estar com todas as suas contas recebidas')
def step_impl(context):
    for it in context.promisoria.contas:
        assert it.recebida == True
