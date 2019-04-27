from pyflunt.notifications import Notifiable
from pyflunt.validations import Contract


class Name(Notifiable):
    def __init__(self, name):
        super().__init__()

        self._name = name

        contract = Contract().requires().is_not_none_or_white_space(value=name,
                                                                    field='name',
                                                                    message='invalid name')
        self.add_notifications(contract)

    def __str__(self):
        return self._name


class Cpf(Notifiable):
    def __init__(self, cpf):
        super().__init__()

        self._cpf = cpf

        contract = Contract().requires().has_len(value=cpf,
                                                 length=11,
                                                 field='cpf',
                                                 message='invalid cpf')

        self.add_notifications(contract)

    def __str__(self):
        return self._cpf


class Email(Notifiable):
    def __init__(self, email):
        super().__init__()

        self._email = email

        contract = Contract().requires().is_email(value=email,
                                                  field='email',
                                                  message='invalid email')

        self.add_notifications(contract)

    def __str__(self):
        return self._email
