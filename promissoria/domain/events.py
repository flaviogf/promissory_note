from common.domain.events import Event


class EmitenteCadastrado(Event):
    def __init__(self, nome: 'str', cpf: 'str', endereco: 'str'):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
