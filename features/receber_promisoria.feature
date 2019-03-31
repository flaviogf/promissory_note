# language: pt

Funcionalidade: receber promisoria
    como um usuario
    eu quero ser capaz de receber uma promisoria
    para que eu saiba o valor das minhas contas recebidas

    Cenario: realizar o recebimento
    Dado uma promisoria
    Quando solicitado seu recebimento
    Entao a promisoria deve ser marcada como recebida
    E um evento de promisoria recebida deve ser acionado
