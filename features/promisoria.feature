Funcionalidade: receber promisoria
Cenario: receber uma promisoria com sucesso
    Dado uma promisoria
    Quando informado o beneficiario da promisoria
    E solicitado o recebimento da promisoria
    Entao a promisoria deve estar marcada como recebida
    E a promisoria deve ter uma data de recebimento
    E a promisoria deve estar com todas as suas contas recebidas
