import unittest

from promissory_note.entities import Beneficiary, Emitter
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
        address = 'New'
        email = Email('captain@marvel.com.br')

        emitter = Emitter(name=name,
                          cpf=cpf,
                          address=address,
                          email=email)

        self.assertFalse(emitter.is_valid)

    def test_should_notifications_must_contain_invalid_address_message_when_address_is_invalid(self):
        name = Name('Steve')
        cpf = Cpf('11111111199')
        address = 'New'
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
