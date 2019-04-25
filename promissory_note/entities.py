from pyflunt.notifications import Notifiable
from pyflunt.validations import Contract


class Beneficiary(Notifiable):
    def __init__(self, name, cpf, email):
        super().__init__()
        self._name = name
        self._cpf = cpf
        self._email = email

        self.add_notifications(name, cpf, email)


class Emitter(Notifiable):
    def __init__(self, name, cpf, address, email):
        super().__init__()
        self._name = name
        self._cpf = cpf
        self._address = address
        self._email = email

        contract = Contract().requires().has_min_len(value=address,
                                                     minimum=6,
                                                     field='address',
                                                     message='invalid address')

        self.add_notifications(contract, name, cpf, email)
