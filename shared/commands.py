"""modulo dos comandos do shared"""


class Command:
    """classe base para os comandos"""
    ...


class CommandResult:
    """classe base para os resultados dos comandos"""

    def __init__(self, status: bool = True, mensagem: str = ''):
        self.status = status
        self.mensagem = mensagem
