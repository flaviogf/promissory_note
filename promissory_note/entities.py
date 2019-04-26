from datetime import date

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

        contract = Contract().requires().is_not_none_or_white_space(value=address,
                                                                    field='address',
                                                                    message='invalid address')

        self.add_notifications(contract, name, cpf, email)


class PromissoryNote(Notifiable):
    def __init__(self,
                 number,
                 due_date,
                 value,
                 currency,
                 city_payment,
                 state_payment,
                 issuance_date,
                 beneficiary,
                 emitter):
        super().__init__()

        self._number = number
        self._due_date = due_date
        self._value = value
        self._currency = currency
        self._city_payment = city_payment
        self._state_payment = state_payment
        self._issuance_date = issuance_date
        self._beneficiary = beneficiary
        self._emitter = emitter
        self._subscribers = []

        contract = (Contract().requires()
                    .is_greater_than(value=number,
                                     comparer=0,
                                     field='number',
                                     message='number should be greater than zero')
                    .is_greater_or_equals_than(value=due_date,
                                               comparer=date.today(),
                                               field='due date',
                                               message='date should be greater or equals than today')
                    .is_greater_than(value=value,
                                     comparer=0,
                                     field='value',
                                     message='value should be greater than zero')
                    .is_not_none_or_white_space(value=currency,
                                                field='currency',
                                                message='invalid currency')
                    .is_not_none_or_white_space(value=city_payment,
                                                field='city payment',
                                                message='invalid city payment')
                    .is_not_none_or_white_space(value=state_payment,
                                                field='state payment',
                                                message='invalid state payment')
                    .is_greater_or_equals_than(value=issuance_date,
                                               comparer=date.today(),
                                               field='issuance date',
                                               message='issuance date should be greater or equals than today'))

        self.add_notifications(contract, beneficiary, emitter)

    @property
    def subscribers(self):
        return tuple(self._subscribers)

    def add_subscribers(self, subscriber):
        self._subscribers.append(subscriber)
