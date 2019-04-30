import unittest
from datetime import date, datetime
from os import chdir, listdir, path, remove
from unittest.mock import patch, Mock

from pyfiglet import Figlet

from promissory_note.gateways.cli import Cli, print_green, print_blue, print_application_name, print_description, main
from promissory_note.gateways.services import CONTENT_DIR, PROMISSORY_NOTE_IMAGE, OPEN_SANS


class PrintBlueTests(unittest.TestCase):
    @patch('builtins.print')
    def test_should_print_text_when_print_green_is_called_with_text(self, print):
        print_blue('Tony', begin='\n')

        print.assert_called_with('\033[34m\nTony\033[0m')


class PrintGreenTests(unittest.TestCase):
    @patch('builtins.print')
    def test_should_print_text_when_print_green_is_called_with_text(self, print):
        print_green('Tony', begin='\n')

        print.assert_called_with('\033[32m\nTony\033[0m')


class PrintApplicationNameTests(unittest.TestCase):
    @patch('promissory_note.gateways.cli.print_blue')
    def test_should_print_application_name_when_is_called(self, print_blue):
        font = Figlet(font='pepper')
        application_name = font.renderText('Promissory Note')

        print_application_name()

        print_blue.assert_called_with(application_name)


class PrintDescriptionTests(unittest.TestCase):
    @patch('promissory_note.gateways.cli.print_blue')
    def test_should_print_description_when_is_called(self, print_blue):
        description = 'Welcome, send your promissory notes'

        print_description()

        print_blue.assert_called_with(description, end='\n\n')


class CliTests(unittest.TestCase):
    def setUp(self):
        self._cli = Cli()

        self._cli._image_generation_service = Mock()
        self._cli._email_service = Mock()
        self._cli._issue_promissory_note = Mock()

        self._execute_issued_promissory_note()
        self._remove_created_images()

    def tearDown(self):
        self._remove_created_images()

    def test_should_cli_print_promissory_note_issued_success(self):
        self._cli._issue_promissory_note.execute.assert_called_once()

    def test_should_cli_contains_number(self):
        self.assertEqual(1, self._cli.number)

    def test_should_cli_contains_due_date(self):
        self.assertEqual(date(year=2020, month=12, day=12), self._cli.due_date)

    def test_should_cli_contains_value(self):
        self.assertEqual(100.99, self._cli.value)

    def test_should_cli_contains_beneficiary_name(self):
        self.assertEqual('Steve', self._cli.beneficiary_name)

    def test_should_cli_contains_beneficiary_cpf(self):
        self.assertEqual('11111111199', self._cli.beneficiary_cpf)

    def test_should_cli_contains_beneficiary_email(self):
        self.assertEqual('captain@marvel.com', self._cli.beneficiary_email)

    def test_should_cli_contains_currency(self):
        self.assertEqual('real', self._cli.currency)

    def test_should_cli_contains_city_payment(self):
        self.assertEqual('New York', self._cli.city_payment)

    def test_should_cli_contains_state_payment(self):
        self.assertEqual('New York', self._cli.state_payment)

    def test_should_cli_contains_emitter_name(self):
        self.assertEqual('Tony Stark', self._cli.emitter_name)

    def test_should_cli_contains_emitter_cpf(self):
        self.assertEqual('11111111188', self._cli.emitter_cpf)

    def test_should_cli_contains_emitter_address(self):
        self.assertEqual('New York', self._cli.emitter_address)

    def test_should_cli_contains_emitter_email(self):
        self.assertEqual('iron_man@marvel.com', self._cli.emitter_email)

    def test_should_cli_contains_issuance_date(self):
        self.assertEqual(date(year=2020, month=12, day=12), self._cli.issuance_date)

    def _execute_issued_promissory_note(self):
        self._cli.issued_promissory_note(number=1,
                                         due_date=datetime(day=12, month=12, year=2020),
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
                                         issuance_date=datetime(day=12, month=12, year=2020))

    def _remove_created_images(self):
        chdir(CONTENT_DIR)

        created_images = [file for file in listdir(CONTENT_DIR) if
                          file not in (path.basename(PROMISSORY_NOTE_IMAGE), path.basename(OPEN_SANS))]

        for image in created_images:
            remove(image)


class MainTests(unittest.TestCase):
    @patch('promissory_note.gateways.cli.print_application_name')
    @patch('promissory_note.gateways.cli.print_description')
    @patch('promissory_note.gateways.cli.issue_promissory_note')
    def test_should_main_called_print_application_name(self,
                                                       print_application_name,
                                                       print_description,
                                                       issue_promissory_note):
        main()

        print_application_name.assert_called_once()

    @patch('promissory_note.gateways.cli.print_application_name')
    @patch('promissory_note.gateways.cli.print_description')
    @patch('promissory_note.gateways.cli.issue_promissory_note')
    def test_should_main_called_print_description(self,
                                                  print_application_name,
                                                  print_description,
                                                  issue_promissory_note):
        main()

        print_description.assert_called_once()

    @patch('promissory_note.gateways.cli.print_application_name')
    @patch('promissory_note.gateways.cli.print_description')
    @patch('promissory_note.gateways.cli.issue_promissory_note')
    def test_should_main_called_issue_promissory_note(self,
                                                      print_application_name,
                                                      print_description,
                                                      issue_promissory_note):
        main()

        issue_promissory_note.assert_called_once()
