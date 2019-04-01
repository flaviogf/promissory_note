from domain.core.services import EmailService


class RabbitEmailService(EmailService):
    def envia(self, destinatario: 'str', corpo: 'str'):
        ...
