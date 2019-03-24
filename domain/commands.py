"""modulo de comandos do dominio"""
from shared.commands import Command, CommandResult


class CriarPromisoriaCommand(Command):
    """classe que representa um comando para a criação de uma promisória"""
    ...

    def __init__(self):
        self.id_emitente = None
        self.id_beneficario = None
        self.id_contas = []


class CriarPromisoriaCommandResult(CommandResult):
    """classe que representa o resultado do comando de criar promisória"""
    ...
