import unittest

from promissory_note.value_objects import Name, Cpf, Email


class NameTests(unittest.TestCase):
    def test_should_is_valid_true_when_name_is_not_empty_or_white_space(self):
        name = Name('Steve')

        self.assertTrue(name.is_valid)

    def test_should_is_valid_false_when_name_is_empty(self):
        name = Name('')

        self.assertFalse(name.is_valid)

    def test_should_is_valid_false_when_name_is_none(self):
        name = Name(None)

        self.assertFalse(name.is_valid)

    def test_should_notification_must_contain_invalid_name_message_when_name_is_invalid(self):
        name = Name('')

        notification = name.notifications[0]

        self.assertEqual('invalid name', notification.message)

    def test_should_str_return_name_string(self):
        name = Name('Steve')

        self.assertEqual('Steve', str(name))


class CpfTests(unittest.TestCase):
    def test_should_is_valid_true_when_length_cpf_is_equal_to_eleven(self):
        cpf = Cpf('11111111111')

        self.assertTrue(cpf.is_valid)

    def test_should_is_valid_false_when_length_cpf_is_not_equal_to_eleven(self):
        cpf = Cpf('1111111111')

        self.assertFalse(cpf.is_valid)

    def test_should_notification_must_contain_invalid_cpf_message_when_cpf_is_invalid(self):
        cpf = Cpf('1111111111')

        notification = cpf.notifications[0]

        self.assertEqual('invalid cpf', notification.message)

    def test_should_str_return_cpf_string(self):
        cpf = Cpf('11111111111')

        self.assertEqual('11111111111', str(cpf))


class EmailTests(unittest.TestCase):
    def test_should_is_valid_true_when_email_is_valid(self):
        email = Email('steve@marvel.com')

        self.assertTrue(email.is_valid)

    def test_should_is_valid_false_when_email_is_invalid(self):
        email = Email('anything')

        self.assertFalse(email.is_valid)

    def test_should_notification_must_contain_invalid_email_message_when_email_is_invalid(self):
        email = Email('anything')

        notification = email.notifications[0]

        self.assertEqual('invalid email', notification.message)

    def test_should_str_return_email_string(self):
        email = Email('captain@marvel.com')

        self.assertEqual('captain@marvel.com', str(email))
