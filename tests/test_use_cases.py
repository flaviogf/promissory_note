import unittest
from datetime import date
from unittest.mock import Mock

from promissory_note.commands import IssuePromissoryNoteCommand
from promissory_note.use_cases import IssuePromissoryNote


class IssuePromissoryNoteTests(unittest.TestCase):
    def setUp(self):
        self._image_generation_service = Mock()
        self._email_promissory_note_issued = Mock()

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

        self._issue_promissory_note = IssuePromissoryNote(
            image_generation_service=self._image_generation_service,
            email_promissory_note_issued=self._email_promissory_note_issued)

    def test_should_image_generation_service_is_called_when_promissory_note_is_issued(self):
        self._issue_promissory_note.execute(command=self._issue_promissory_note_command)

        self._image_generation_service.assert_called_once()

    def test_should_email_service_is_called_when_promissory_note_is_issued(self):
        self._issue_promissory_note.execute(command=self._issue_promissory_note_command)

        self._email_promissory_note_issued.assert_called_once()
