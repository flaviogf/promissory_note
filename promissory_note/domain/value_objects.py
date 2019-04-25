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
