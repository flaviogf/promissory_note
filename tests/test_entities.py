import unittest
from datetime import date, timedelta
from unittest.mock import Mock

from promissory_note.entities import Beneficiary, Emitter, PromissoryNote
from promissory_note.events import PromissoryNoteIssued, PromissoryNoteNotIssued
from promissory_note.value_objects import Name, Email, Cpf


class BeneficiaryTests(unittest.TestCase):
    def setUp(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        email = Email('captain@marvel.com')

        self._beneficiary = Beneficiary(name=name,
                                        cpf=cpf,
                                        email=email)

    def test_should_is_valid_true_when_all_properties_are_valid(self):
        self.assertTrue(self._beneficiary.is_valid)

    def test_should_is_valid_false_when_name_is_invalid(self):
        name = Name(None)
        cpf = Cpf('11111111199')
        email = Email('captain@marvel.com')

        beneficiary = Beneficiary(name=name,
                                  cpf=cpf,
                                  email=email)

        self.assertFalse(beneficiary.is_valid)

    def test_should_is_valid_false_when_cpf_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('1111111119')
        email = Email('captain@marvel.com')

        beneficiary = Beneficiary(name=name,
                                  cpf=cpf,
                                  email=email)

        self.assertFalse(beneficiary.is_valid)

    def test_should_is_valid_false_when_email_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        email = Email('invalid email')

        beneficiary = Beneficiary(name=name,
                                  cpf=cpf,
                                  email=email)

        self.assertFalse(beneficiary.is_valid)

    def test_should_contains_property_name(self):
        self.assertEqual('Steve', self._beneficiary.name)

    def test_should_contains_property_cpf(self):
        self.assertEqual('11111111199', self._beneficiary.cpf)

    def test_should_contains_property_email(self):
        self.assertEqual('captain@marvel.com', self._beneficiary.email)


class EmitterTests(unittest.TestCase):
    def setUp(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = 'New York'
        email = Email('captain@marvel.com')

        self._emitter = Emitter(name=name,
                                cpf=cpf,
                                address=address,
                                email=email)

    def test_should_is_valid_true_when_all_properties_are_valid(self):
        self.assertTrue(self._emitter.is_valid)

    def test_should_is_valid_false_when_name_is_invalid(self):
        name = Name('')
        cpf = Cpf('11111111199')
        address = 'New York'
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertFalse(emitter.is_valid)

    def test_should_is_valid_false_when_cpf_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('1111111119')
        address = 'New York'
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertFalse(emitter.is_valid)

    def test_should_is_valid_false_when_address_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = ''
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertFalse(emitter.is_valid)

    def test_should_notifications_must_contain_invalid_address_message_when_address_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = ''
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        invalid_address_notification = emitter.notifications[0]

        self.assertEqual('invalid address', invalid_address_notification.message)

    def test_should_is_valid_false_when_email_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = 'New York'
        email = Email('invalid email')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertFalse(emitter.is_valid)

    def test_should_contains_property_name(self):
        self.assertEqual('Steve', self._emitter.name)

    def test_should_contains_property_cpf(self):
        self.assertEqual('11111111199', self._emitter.cpf)

    def test_should_contains_property_address(self):
        self.assertEqual('New York', self._emitter.address)

    def test_should_contains_property_email(self):
        self.assertEqual('captain@marvel.com', self._emitter.email)


class PromissoryNoteTests(unittest.TestCase):
    def setUp(self):
        number = 1
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com'))

        self._promissory_note = PromissoryNote(number=number,
                                               due_date=due_date,
                                               value=value,
                                               currency=currency,
                                               city_payment=city_payment,
                                               state_payment=state_payment,
                                               issuance_date=issuance_date,
                                               beneficiary=beneficiary,
                                               emitter=emitter)

    def test_should_is_valid_true_when_all_properties_are_valid(self):
        self.assertTrue(self._promissory_note.is_valid)

    def test_should_is_valid_false_when_number_is_invalid(self):
        number = 0
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_due_date_is_invalid(self):
        number = 1
        due_date = date.today() - timedelta(days=1)
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_value_is_invalid(self):
        number = 1
        due_date = date.today()
        value = 0
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_currency_is_invalid(self):
        number = 1
        due_date = date.today()
        value = 100.99
        currency = ''
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_city_payment_is_invalid(self):
        number = 1
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = ''
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_state_payment_is_invalid(self):
        number = 1
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = ''
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_is_valid_false_when_issuance_date_is_invalid(self):
        number = 1
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today() - timedelta(days=1)

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        self.assertFalse(promissory_note.is_valid)

    def test_should_add_subscriber_when_add_subscribers_is_called_with_a_callable(self):
        email_service = Mock()

        self._promissory_note.attach(email_service)

        self.assertEqual(1, len(self._promissory_note.subscribers))

    def test_should_call_subscribers_with_promissory_note_issued_when_issue_is_called_and_promissory_is_valid(self):
        promissory_note_issued = PromissoryNoteIssued(number=1,
                                                      due_date=date.today(),
                                                      value=100.99,
                                                      beneficiary_name='Steve',
                                                      beneficiary_cpf='11111111199',
                                                      beneficiary_email='captain@marvel.com',
                                                      currency='real',
                                                      city_payment='New York',
                                                      state_payment='New York',
                                                      emitter_name='Tony Stark',
                                                      emitter_cpf='11111111188',
                                                      emitter_address='New York',
                                                      emitter_email='iron_man@marvel.com',
                                                      issuance_date=date.today())

        email_service = Mock()

        self._promissory_note.attach(email_service)

        self._promissory_note.issue()

        email_service.assert_called_once_with(promissory_note_issued)

    def test_should_call_subscribers_with_promissory_note_not_issued_when_issue_is_called_and_promissory_is_valid(self):
        number = 0
        due_date = date.today()
        value = 100.99
        currency = 'real'
        city_payment = 'New York'
        state_payment = 'New York'
        issuance_date = date.today()

        beneficiary = Beneficiary(name=Name('Steve'),
                                  cpf=Cpf('11111111199'),
                                  email=Email('captain@marvel.com'))

        emitter = Emitter(name=Name('Tony Stark'),
                          cpf=Cpf('11111111188'),
                          address='New York',
                          email=Email('iron_man@marvel.com.br'))

        promissory_note = PromissoryNote(number=number,
                                         due_date=due_date,
                                         value=value,
                                         currency=currency,
                                         city_payment=city_payment,
                                         state_payment=state_payment,
                                         issuance_date=issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        promissory_note_not_issued = PromissoryNoteNotIssued(notifications=promissory_note.notifications)

        email_service = Mock()

        promissory_note.attach(email_service)

        promissory_note.issue()

        email_service.assert_called_once_with(promissory_note_not_issued)
