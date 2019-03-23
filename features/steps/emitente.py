from behave import given, then, when

from domain.entities import Emitente


@given(u'um emitente')
def step_impl(context):
    context.emitente = Emitente(nome='Flavio',
                                telefone='016999999999',
                                endereco='Rua y')


@when(u'o emitente emite um promisoria')
def step_impl(context):
    context.promisoria = context.emitente.emite_promisoria()


@then(u'entao a promisoria deve estar vinculada ao emitente')
def step_impl(context):
    assert context.promisoria.emitente == context.emitente
