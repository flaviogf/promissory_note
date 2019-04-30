from datetime import date

import click
from pyfiglet import Figlet

from promissory_note.commands import IssuePromissoryNoteCommand
from promissory_note.gateways.services import PillowImageGenerationService, SendGridEmailPromissoryNoteIssued
from promissory_note.use_cases import IssuePromissoryNote


def print_blue(text, begin='', *args, **kwargs):
    print(f'\033[34m{begin}{text}\033[0m', *args, **kwargs)


def print_green(text, begin='', *args, **kwargs):
    print(f'\033[32m{begin}{text}\033[0m', *args, **kwargs)


def print_application_name():
    font = Figlet(font='pepper')
    application_name = font.renderText('Promissory Note')
    print_blue(application_name)


def print_description():
    description = 'Welcome, send your promissory notes'
    print_blue(description, end='\n\n')


@click.command()
@click.option('--number',
              default=1,
              prompt=True,
              type=click.INT)
@click.option('--due-date',
              default=date.today().strftime('%d/%m/%Y'),
              prompt=True,
              type=click.DateTime(('%d/%m/%Y',)))
@click.option('--value',
              default=100.99,
              prompt=True,
              type=click.FLOAT)
@click.option('--beneficiary-name',
              default='Steve',
              prompt=True,
              type=click.STRING)
@click.option('--beneficiary-cpf',
              default='11111111199',
              prompt=True,
              type=click.STRING)
@click.option('--beneficiary-email',
              default='captain@marvel.com',
              prompt=True,
              type=click.STRING)
@click.option('--currency',
              default='dollar',
              prompt=True,
              type=click.STRING)
@click.option('--city-payment',
              default='New York',
              prompt=True,
              type=click.STRING)
@click.option('--state-payment',
              default='New York',
              prompt=True,
              type=click.STRING)
@click.option('--emitter-name',
              default='Tony Stark',
              prompt=True,
              type=click.STRING)
@click.option('--emitter-cpf',
              default='11111111188',
              prompt=True,
              type=click.STRING)
@click.option('--emitter-address',
              default='New York',
              prompt=True,
              type=click.STRING)
@click.option('--emitter-email',
              default='iron_man@marveil.com',
              prompt=True,
              type=click.STRING)
@click.option('--issuance-date',
              default=date.today().strftime('%d/%m/%Y'),
              prompt=True,
              type=click.DateTime(('%d/%m/%Y',)))
def issue_promissory_note(number,
                          due_date,
                          value,
                          beneficiary_name,
                          beneficiary_cpf,
                          beneficiary_email,
                          currency,
                          city_payment,
                          state_payment,
                          emitter_name,
                          emitter_cpf,
                          emitter_address,
                          emitter_email,
                          issuance_date):
    Cli().issued_promissory_note(number,
                                 due_date,
                                 value,
                                 beneficiary_name,
                                 beneficiary_cpf,
                                 beneficiary_email,
                                 currency,
                                 city_payment,
                                 state_payment,
                                 emitter_name,
                                 emitter_cpf,
                                 emitter_address,
                                 emitter_email,
                                 issuance_date)


class Cli:
    def __init__(self):
        self._image_generation_service = PillowImageGenerationService()
        self._email_service = SendGridEmailPromissoryNoteIssued()

        self._issue_promissory_note = IssuePromissoryNote(self._image_generation_service, self._email_service)

        self._number = None
        self._due_date = None
        self._value = None
        self._beneficiary_name = None
        self._beneficiary_cpf = None
        self._beneficiary_email = None
        self._currency = None
        self._city_payment = None
        self._state_payment = None
        self._emitter_name = None
        self._emitter_cpf = None
        self._emitter_address = None
        self._emitter_email = None
        self._issuance_date = None

        self._issue_promissory_note_command = None

    @property
    def number(self):
        return self._number

    @property
    def due_date(self):
        return self._due_date.date()

    @property
    def value(self):
        return self._value

    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @property
    def beneficiary_cpf(self):
        return self._beneficiary_cpf

    @property
    def beneficiary_email(self):
        return self._beneficiary_email

    @property
    def currency(self):
        return self._currency

    @property
    def city_payment(self):
        return self._city_payment

    @property
    def state_payment(self):
        return self._state_payment

    @property
    def emitter_name(self):
        return self._emitter_name

    @property
    def emitter_cpf(self):
        return self._emitter_cpf

    @property
    def emitter_address(self):
        return self._emitter_address

    @property
    def emitter_email(self):
        return self._emitter_email

    @property
    def issuance_date(self):
        return self._issuance_date.date()

    def issued_promissory_note(self,
                               number,
                               due_date,
                               value,
                               beneficiary_name,
                               beneficiary_cpf,
                               beneficiary_email,
                               currency,
                               city_payment,
                               state_payment,
                               emitter_name,
                               emitter_cpf,
                               emitter_address,
                               emitter_email,
                               issuance_date):
        self._number = number
        self._due_date = due_date
        self._value = value
        self._beneficiary_name = beneficiary_name
        self._beneficiary_cpf = beneficiary_cpf
        self._beneficiary_email = beneficiary_email
        self._currency = currency
        self._city_payment = city_payment
        self._state_payment = state_payment
        self._emitter_name = emitter_name
        self._emitter_cpf = emitter_cpf
        self._emitter_address = emitter_address
        self._emitter_email = emitter_email
        self._issuance_date = issuance_date

        self._create_command()

        self._issue_promissory_note.execute(command=self._issue_promissory_note_command)

        print_green('Emission request sent !!!', begin='\n\n')

    def _create_command(self):
        self._issue_promissory_note_command = IssuePromissoryNoteCommand(number=self.number,
                                                                         due_date=self.due_date,
                                                                         value=self.value,
                                                                         beneficiary_name=self.beneficiary_name,
                                                                         beneficiary_cpf=self.beneficiary_cpf,
                                                                         beneficiary_email=self.beneficiary_email,
                                                                         currency=self.currency,
                                                                         city_payment=self.city_payment,
                                                                         state_payment=self.state_payment,
                                                                         emitter_name=self.emitter_name,
                                                                         emitter_cpf=self.emitter_cpf,
                                                                         emitter_address=self.emitter_address,
                                                                         emitter_email=self.emitter_email,
                                                                         issuance_date=self.issuance_date)


def main():
    print_application_name()
    print_description()
    issue_promissory_note()


if __name__ == '__main__':
    main()
