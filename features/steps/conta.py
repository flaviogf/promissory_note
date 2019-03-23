from datetime import datetime

from behave import given, then, when

from domain.entities import Conta


@given('uma conta')
def step_impl(context):
    context.conta = Conta(descricao='conta x', valor=100.00)


@when('solicitado o recebimento da conta')
def step_impl(context):
    context.conta.recebe()


@then('a conta deve estar marcada como recebida')
def step_impl(context):
    assert context.conta.recebida == True


@then('a conta deve ter uma data de recebimento')
def step_impl(context):
    assert type(context.conta.data_recebimento) == datetime
