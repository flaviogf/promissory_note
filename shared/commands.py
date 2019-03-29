class Command:
    ...


class CommandResult:
    def __init__(self, status: bool = True, mensagem: str = ''):
        self.status = status
        self.mensagem = mensagem
