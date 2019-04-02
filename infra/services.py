from json import dumps

from pika.exceptions import AMQPConnectionError

from domain.core.services import EmailService


class RabbitEmailService(EmailService):
    def __init__(self, get_rabbit_connection):
        self.get_rabbit_connection = get_rabbit_connection

    def envia(self, destinatario: 'str', email: 'str'):
        try:
            connection = self.get_rabbit_connection()
            channel = connection.channel()
            channel.exchange_declare(exchange='email_promissoria', exchange_type='fanout')
            body = dumps({'destinatario': destinatario, 'email': email})
            channel.basic_publish(exchange='email_promissoria', routing_key='', body=body)
            connection.close()
        except AMQPConnectionError:
            ...
