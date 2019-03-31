# language: pt

Funcionalidade: solicitar promissoria
    como um usuario
    eu quero ser capaz de solicitar uma promissoria
    para controlar minhas contas a receber

    Cenario: realizar a solicitacao
    Dado um numero
    E um data de vencimento
    E um valor
    E um beneficiario
    E um emitente
    Quando solicitar uma promisoria
    Entao o evento de promisoria solicitada deve ser acionado
