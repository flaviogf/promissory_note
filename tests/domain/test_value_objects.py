import unittest

from promissory_note.domain.value_objects import Name


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

    def test_should_notification_has_message_invalid_name(self):
        name = Name('')

        notification = name.notifications[0]

        self.assertEqual('invalid name', notification.message)
