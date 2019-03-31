# language: pt

Funcionalidade: solicitar promissoria
    como um usuario
    eu quero ser capaz de solicitar uma promissoria
    para controlar minhas contas a receber

    Cenario: realizar a solicitacao
    Dado um beneficiario
    E um emitente
    E um valor
    Quando solicitar uma promisoria
    Entao o evento de promisoria solicitada deve ser acionado
