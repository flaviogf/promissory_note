from os import path
from os.path import dirname

from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = dirname(dirname(dirname(__file__)))

CONTENT_DIR = path.join(ROOT_DIR, 'content')

PROMISSORY_NOTE_IMAGE = path.join(CONTENT_DIR, 'promissory_note.jpg')

OPEN_SANS = path.join(CONTENT_DIR, 'open_sans.ttf')

TEXT_FONT = ImageFont.truetype(OPEN_SANS, size=16)

TEXT_COLOR = 'rgb(0,0,0)'

NUMBER_POSITION = 200, 32

DUE_DATE_DAY_POSITION = 348, 32

DUE_DATE_MONTH_POSITION = 410, 32


class PillowImageGenerationService:
    def __init__(self):
        self._image = None
        self._draw = None
        self._filename = None
        self._promissory_note_issued = None

    def __call__(self, promissory_note_issued):
        return self.generate(promissory_note_issued)

    def generate(self, promissory_note_issued):
        self._promissory_note_issued = promissory_note_issued

        self._open_image()

        self._write_number()
        self._write_due_date()
        self._write_value()
        self._write_beneficiary_name()
        self._write_beneficiary_cpf()
        self._write_currency()
        self._write_city_payment()
        self._write_emitter_name()
        self._write_issuance_date()
        self._write_emitter_cpf()
        self._write_emitter_address()

        self._create_filename()

        self._save_image()

    def _open_image(self):
        self._image = Image.open(PROMISSORY_NOTE_IMAGE)
        self._draw = ImageDraw.Draw(self._image)

    def _write_number(self):
        self._draw.text(NUMBER_POSITION, str(self._promissory_note_issued.number), fill=TEXT_COLOR, font=TEXT_FONT)

    def _create_filename(self):
        basename = f'{self._promissory_note_issued.number}_promissory_note.jpg'
        self._filename = path.join(CONTENT_DIR, basename)

    def _save_image(self):
        self._image.save(self._filename)

    def _write_due_date(self):
        day = self._promissory_note_issued.due_date.strftime('%d')
        month = self._promissory_note_issued.due_date.strftime('%B')
        self._draw.text(DUE_DATE_DAY_POSITION, day, fill=TEXT_COLOR, font=TEXT_FONT)
        self._draw.text(DUE_DATE_MONTH_POSITION, month, fill=TEXT_COLOR, font=TEXT_FONT)
        pass

    def _write_value(self):
        # TODO: write value
        pass

    def _write_beneficiary_name(self):
        # TODO: write beneficiary name
        pass

    def _write_beneficiary_cpf(self):
        # TODO: write beneficiary cpf
        pass

    def _write_currency(self):
        # TODO: write currency
        pass

    def _write_city_payment(self):
        # TODO: write city payment
        pass

    def _write_emitter_name(self):
        # TODO: write emitter name
        pass

    def _write_issuance_date(self):
        # TODO: write issuance date
        pass

    def _write_emitter_cpf(self):
        # TODO: write emitter cpf
        pass

    def _write_emitter_address(self):
        # TODO: write emitter address
        pass
