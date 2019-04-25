import unittest

from promissory_note.entities import Beneficiary
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
