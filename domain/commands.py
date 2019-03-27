"""modulo de comandos do dominio"""
from shared.commands import Command, CommandResult


class EmitirPromisoriaCommand(Command):
    """classe que representa um comando para a emição de uma promisória"""
    ...

    def __init__(self):
        self.id_emitente = None
        self.id_beneficario = None
        self.id_contas = []


class EmitirPromisoriaCommandResult(CommandResult):
    """classe que representa o resultado do comando de emição de uma promisória"""
    ...
