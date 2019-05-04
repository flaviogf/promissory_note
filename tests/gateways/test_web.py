import unittest
from datetime import date
from unittest.mock import patch

from promissory_note.gateways.web import app, IssuePromissoryNoteForm


class IssuePromissoryNoteFormTests(unittest.TestCase):
    def test_should_returns_true_when_validate_is_called_with_form_valid(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertTrue(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_number(self):
        data = {
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_due_date(self):
        data = {
            'number': 100,
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_value(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_beneficiary_name(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }
        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_beneficiary_cpf(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }
        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_beneficiary_email(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_currency(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_city_payment(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_state_payment(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_emitter_name(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_emitter_cpf(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_emitter_address(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_emitter_email(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_returns_false_when_issue_note_promissory_note_does_not_contains_issuance_date(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertFalse(issue_promissory_note_form.validate())

    def test_should_due_data_of_data_returns_instance_of_datetime(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertIsInstance(issue_promissory_note_form.data['due_date'], date)

    def test_should_issuance_date_of_data_returns_instance_of_datetime(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertIsInstance(issue_promissory_note_form.data['issuance_date'], date)

    def test_should_number_of_data_returns_instance_of_int(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertIsInstance(issue_promissory_note_form.data['number'], int)

    def test_should_value_of_data_returns_instance_of_float(self):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        issue_promissory_note_form = IssuePromissoryNoteForm(data=data)

        self.assertIsInstance(issue_promissory_note_form.data['value'], float)


class AppTests(unittest.TestCase):
    def test_should_returns_status_ok_when_send_request_to_index(self):
        client = app.test_client()

        response = client.get('/')

        self.assertEqual(200, response.status_code)

    def test_should_returns_template_with_title_promissory_note_when_send_request_to_index(self):
        client = app.test_client()

        response = client.get('/')

        self.assertTrue(b'Promissory Note' in response.data)

    @patch('promissory_note.gateways.web.PillowImageGenerationService')
    @patch('promissory_note.gateways.web.SendGridEmailPromissoryNoteIssued')
    def test_should_returns_status_redirects_when_post_request_is_valid(self,
                                                                        pillow_image_generation_service,
                                                                        send_grid_email_promissory_note_issued):
        data = {
            'number': 100,
            'due_date': date.today().strftime('%d/%m/%Y'),
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
            'issuance_date': date.today().strftime('%d/%m/%Y'),
        }

        client = app.test_client()

        response = client.post('/', data=data)

        self.assertEqual(302, response.status_code)

    @patch('promissory_note.gateways.web.PillowImageGenerationService')
    @patch('promissory_note.gateways.web.SendGridEmailPromissoryNoteIssued')
    def test_should_returns_status_ok_when_post_request_is_invalid(self,
                                                                   pillow_image_generation_service,
                                                                   send_grid_email_promissory_note_issued):
        data = {
            'number': 100,
            'value': 100,
            'beneficiary_name': 'Steve',
            'beneficiary_cpf': '00000000000',
            'beneficiary_email': 'captain@marvel.com.br',
            'currency': 'dollar',
            'city_payment': 'New York',
            'state_payment': 'New York',
            'emitter_name': 'Tony Stark',
            'emitter_cpf': '99999999999',
            'emitter_address': 'New York',
            'emitter_email': 'iron_man@marvel.com',
        }

        client = app.test_client()

        response = client.post('/', data=data)

        self.assertEqual(200, response.status_code)
