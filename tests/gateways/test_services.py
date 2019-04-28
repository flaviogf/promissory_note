import unittest
from datetime import date
from os import chdir, listdir, remove, path

from promissory_note.events import PromissoryNoteIssued, PromissoryNoteNotIssued
from promissory_note.gateways.services import PillowImageGenerationService, CONTENT_DIR, PROMISSORY_NOTE_IMAGE, \
    OPEN_SANS


class PillowImageGenerationServiceTests(unittest.TestCase):
    def setUp(self):
        self._remove_created_images()

        self._image_generation_service = PillowImageGenerationService()

    def tearDown(self):
        self._remove_created_images()

    def test_should_pillow_image_generation_service_implements_call(self):
        self.assertTrue(callable(self._image_generation_service))

    def test_should_pillow_image_generation_create_image_in_content_dir_when_generate_is_called_with_promissory_note_issued(
            self):
        promissory_note_issued = PromissoryNoteIssued(number=1,
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

        self._image_generation_service.generate(promissory_note_issued=promissory_note_issued)

        filename = f'{promissory_note_issued.number}_promissory_note.jpg'

        self.assertTrue(filename in listdir(CONTENT_DIR))

    def test_should_pillow_image_generation_create_image_in_content_dir_when_call_is_called_with_promissory_note_issued(
            self):
        promissory_note_issued = PromissoryNoteIssued(number=1,
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

        self._image_generation_service(event=promissory_note_issued)

        filename = f'{promissory_note_issued.number}_promissory_note.jpg'

        self.assertTrue(filename in listdir(CONTENT_DIR))

    def test_should_pillow_image_generation_dont_create_image_in_content_dir_when__call_is_called_with_promissory_note_not_issued(
            self):
        created_images = [file for file in listdir(CONTENT_DIR) if
                          file not in (path.basename(PROMISSORY_NOTE_IMAGE), path.basename(OPEN_SANS))]

        promissory_note_not_issued = PromissoryNoteNotIssued(notifications=[])

        self._image_generation_service(event=promissory_note_not_issued)

        self.assertListEqual([], created_images)

    def _remove_created_images(self):
        chdir(CONTENT_DIR)

        created_images = [file for file in listdir(CONTENT_DIR) if
                          file not in (path.basename(PROMISSORY_NOTE_IMAGE), path.basename(OPEN_SANS))]

        for image in created_images:
            remove(image)
