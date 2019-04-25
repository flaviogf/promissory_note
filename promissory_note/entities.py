from pyflunt.notifications import Notifiable


class Beneficiary(Notifiable):
    def __init__(self, name, cpf, email):
        super().__init__()
        self._name = name
        self._cpf = cpf
        self._email = email

        self.add_notifications(name, cpf, email)
