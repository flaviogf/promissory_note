import unittest
from datetime import date, timedelta

from promissory_note.entities import Beneficiary, Emitter, PromissoryNote
from promissory_note.value_objects import Name, Email, Cpf


class BeneficiaryTests(unittest.TestCase):
    def test_should_is_valid_true_when_all_properties_are_valid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        email = Email('captain@marvel.com')

        beneficiary = Beneficiary(name=name,
                                  cpf=cpf,
                                  email=email)

        self.assertTrue(beneficiary.is_valid)

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


class EmitterTests(unittest.TestCase):
    def test_should_is_valid_true_when_all_properties_are_valid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = 'New York'
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertTrue(emitter.is_valid)

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


class PromissoryNoteTests(unittest.TestCase):
    def test_should_is_valid_true_when_all_properties_are_valid(self):
        number = 100
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

        self.assertTrue(promissory_note.is_valid)

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
