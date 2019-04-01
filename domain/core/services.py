from abc import ABC

from domain.shared.services import Service


class EmailService(Service, ABC):
    def envia(self, destinatario: 'str', corpo: 'str'):
        raise NotImplementedError()
