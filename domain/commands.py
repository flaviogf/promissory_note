from shared.commands import Command, CommandResult


class EmitirPromisoriaCommand(Command):
    def __init__(self):
        self.id_emitente = None
        self.id_contas = []


class EmitirPromisoriaCommandResult(CommandResult):
    ...
