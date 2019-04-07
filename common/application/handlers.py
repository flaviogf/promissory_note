from abc import ABC
from typing import Union

from common.application.commands import Command, CommandResult


class Handler(ABC):
    def handle(self, command: 'Command') -> 'Union[None, CommandResult]':
        raise NotImplementedError()
