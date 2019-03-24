from behave import given, then, when

from domain.entities import Beneficiario, Emitente, Promisoria


@given('um beneficiario')
def step_impl(context):
    context.beneficiario = Beneficiario(nome='Flavio',
                                        telefone='016999999999',
                                        endereco='Rua x')

@when('informado a promisoria a receber do beneficiario')
def step_impl(context):
    emitente = Emitente(nome='Fernando',
                        telefone='016999999999',
                        endereco='Rua y')
    context.promisoria = emitente.emite_promisoria()

@when('solicitado o recebimento da promisoria pelo beneficiario')
def step_impl(context):
    context.beneficiario.recebe(context.promisoria)

@then('a lista de promisorias recebidas deve conter a promisoria recebida pelo beneficiario')
def step_impl(context):
    assert context.promisoria in context.beneficiario.promisorias_recebidas
