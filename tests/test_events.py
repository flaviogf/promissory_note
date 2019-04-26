import unittest
from datetime import date

from promissory_note.events import PromissoryNoteIssued, PromissoryNoteNotIssued


class PromissoryNoteIssuedTests(unittest.TestCase):
    def setUp(self):
        self._promissory_note_issued = PromissoryNoteIssued(number=1,
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

    def test_should_promissory_note_issued_contains_number(self):
        self.assertEqual(1, self._promissory_note_issued.number)

    def test_should_promissory_note_issued_contains_due_date(self):
        self.assertEqual(date.today(), self._promissory_note_issued.due_date)

    def test_should_promissory_note_issued_contains_value(self):
        self.assertEqual(100.99, self._promissory_note_issued.value)

    def test_should_promissory_note_issued_contains_beneficiary_name(self):
        self.assertEqual('Steve', self._promissory_note_issued.beneficiary_name)

    def test_should_promissory_note_issued_contains_beneficiary_cpf(self):
        self.assertEqual('11111111199', self._promissory_note_issued.beneficiary_cpf)

    def test_should_promissory_note_issued_contains_beneficiary_email(self):
        self.assertEqual('captain@marvel.com', self._promissory_note_issued.beneficiary_email)

    def test_should_promissory_note_issued_contains_currency(self):
        self.assertEqual('real', self._promissory_note_issued.currency)

    def test_should_promissory_note_issued_contains_city_payment(self):
        self.assertEqual('New York', self._promissory_note_issued.city_payment)

    def test_should_promissory_note_issued_contains_state_payment(self):
        self.assertEqual('New York', self._promissory_note_issued.state_payment)

    def test_should_promissory_note_issued_contains_emitter_name(self):
        self.assertEqual('Tony Stark', self._promissory_note_issued.emitter_name)

    def test_should_promissory_note_issued_contains_emitter_cpf(self):
        self.assertEqual('11111111188', self._promissory_note_issued.emitter_cpf)

    def test_should_promissory_note_issued_contains_emitter_address(self):
        self.assertEqual('New York', self._promissory_note_issued.emitter_address)

    def test_should_promissory_note_issued_contains_emitter_email(self):
        self.assertEqual('iron_man@marvel.com', self._promissory_note_issued.emitter_email)

    def test_should_promissory_note_issued_contains_issuance_date(self):
        self.assertEqual(date.today(), self._promissory_note_issued.issuance_date)

    def test_should_promissory_note_issued_contains_notifications(self):
        self.assertListEqual([], self._promissory_note_issued.notifications)


class PromissoryNoteNotIssuedTests(unittest.TestCase):
    def test_should_promissory_note_not_issued_contains_notifications(self):
        promissory_note_not_issued = PromissoryNoteNotIssued(notifications=[])

        self.assertListEqual([], promissory_note_not_issued.notifications)
