import unittest
from os import chdir, listdir, path, remove
from unittest.mock import patch

from promissory_note.gateways.cli import promissory_note
from promissory_note.gateways.services import CONTENT_DIR, PROMISSORY_NOTE_IMAGE, OPEN_SANS


class CliTests(unittest.TestCase):
    def setUp(self):
        self._remove_created_images()

    def tearDown(self):
        self._remove_created_images()

    @patch('builtins.print')
    def test_should_cli_print_promissory_note_issued_success(self, print):
        promissory_note(number=1,
                        due_date='12/12/2020',
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
                        issuance_date='12/12/2020')

        print.assert_called_with('Emission request sent')

    def _remove_created_images(self):
        chdir(CONTENT_DIR)

        created_images = [file for file in listdir(CONTENT_DIR) if
                          file not in (path.basename(PROMISSORY_NOTE_IMAGE), path.basename(OPEN_SANS))]

        for image in created_images:
            remove(image)
