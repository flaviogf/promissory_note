from common.application.commands import Command


class CadastrarEmitenteCommand(Command):
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
