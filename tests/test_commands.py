import unittest
from datetime import date

from promissory_note.commands import IssuePromissoryNoteCommand


class IssuePromissoryNoteCommandTests(unittest.TestCase):
    def setUp(self):
        self._issue_promissory_note_command = IssuePromissoryNoteCommand(number=1,
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

    def test_should_issue_promissory_note_command_contains_number(self):
        self.assertEqual(1, self._issue_promissory_note_command.number)

    def test_should_issue_promissory_note_command_contains_due_date(self):
        self.assertEqual(date.today(), self._issue_promissory_note_command.due_date)

    def test_should_issue_promissory_note_command_contains_value(self):
        self.assertEqual(100.99, self._issue_promissory_note_command.value)

    def test_should_issue_promissory_note_command_contains_beneficiary_name(self):
        self.assertEqual('Steve', self._issue_promissory_note_command.beneficiary_name)

    def test_should_issue_promissory_note_command_contains_beneficiary_cpf(self):
        self.assertEqual('11111111199', self._issue_promissory_note_command.beneficiary_cpf)

    def test_should_issue_promissory_note_command_contains_beneficiary_email(self):
        self.assertEqual('captain@marvel.com', self._issue_promissory_note_command.beneficiary_email)

    def test_should_issue_promissory_note_command_contains_currency(self):
        self.assertEqual('real', self._issue_promissory_note_command.currency)

    def test_should_issue_promissory_note_command_contains_city_payment(self):
        self.assertEqual('New York', self._issue_promissory_note_command.city_payment)

    def test_should_issue_promissory_note_command_contains_state_payment(self):
        self.assertEqual('New York', self._issue_promissory_note_command.state_payment)

    def test_should_issue_promissory_note_command_contains_emitter_name(self):
        self.assertEqual('Tony Stark', self._issue_promissory_note_command.emitter_name)

    def test_should_issue_promissory_note_command_contains_emitter_cpf(self):
        self.assertEqual('11111111188', self._issue_promissory_note_command.emitter_cpf)

    def test_should_issue_promissory_note_command_contains_emitter_address(self):
        self.assertEqual('New York', self._issue_promissory_note_command.emitter_address)

    def test_should_issue_promissory_note_command_contains_emitter_email(self):
        self.assertEqual('iron_man@marvel.com', self._issue_promissory_note_command.emitter_email)

    def test_should_issue_promissory_note_command_contains_issuance_date(self):
        self.assertEqual(date.today(), self._issue_promissory_note_command.issuance_date)
