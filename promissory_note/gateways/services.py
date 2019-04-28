import locale
from os import path
from os.path import dirname

from PIL import Image, ImageDraw, ImageFont

from promissory_note.events import PromissoryNoteIssued

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

ROOT_DIR = dirname(dirname(__file__))

CONTENT_DIR = path.join(ROOT_DIR, 'content')

PROMISSORY_NOTE_IMAGE = path.join(CONTENT_DIR, 'promissory_note.jpg')

OPEN_SANS = path.join(CONTENT_DIR, 'open_sans.ttf')

TEXT_FONT = ImageFont.truetype(OPEN_SANS, size=16)

TEXT_COLOR = 'rgb(0,0,0)'

NUMBER_POSITION = 200, 34

DUE_DATE_DAY_POSITION = 348, 34

DUE_DATE_MONTH_POSITION = 410, 34

DUE_DATE_YEAR_POSITION = 550, 34

LONG_DUE_DATE_POSITION = 205, 62

VALUE_POSITION = 650, 34

FULL_VALUE_POSITION = 370, 148

BENEFICIARY_NAME_POSITION = 180, 118

BENEFICIARY_NAME_CPF_POSITION = 615, 118

CITY_AND_STATE_PAYMENT_POSITION = 425, 210

EMITTER_NAME_POSITION = 225, 238

ISSUANCE_DATE_DAY_POSITION = 650, 238

ISSUANCE_DATE_MONTH_POSITION = 695, 238

ISSUANCE_DATE_YEAR_POSITION = 735, 238

EMITTER_CPF_POSITION = 225, 264

EMITTER_ADDRESS_POSITION = 525, 264


def write(fn):
    def wrapper(self, *args, **kwargs):
        fn(self, *args, **kwargs)
        self._write()

    return wrapper


class PillowImageGenerationService:
    def __init__(self):
        self._image = None
        self._draw = None
        self._position = None
        self._text = None
        self._filename = None
        self._promissory_note_issued = None

    def __call__(self, event):
        if not isinstance(event, PromissoryNoteIssued):
            return

        self.generate(event)

    def generate(self, promissory_note_issued):
        self._promissory_note_issued = promissory_note_issued

        self._open_image()

        self._write_number()
        self._write_due_date_day()
        self._write_due_date_month()
        self._write_due_date_year()
        self._write_long_due_date()
        self._write_value()
        self._write_full_value()
        self._write_beneficiary_name()
        self._write_beneficiary_cpf()
        self._write_city_and_state_payment()
        self._write_emitter_name()
        self._write_issuance_date_day()
        self._write_issuance_date_month()
        self._write_issuance_date_year()
        self._write_emitter_cpf()
        self._write_emitter_address()

        self._create_filename()

        self._save_image()

    def _open_image(self):
        self._image = Image.open(PROMISSORY_NOTE_IMAGE)
        self._draw = ImageDraw.Draw(self._image)

    @write
    def _write_number(self):
        self._position = NUMBER_POSITION
        self._text = str(self._promissory_note_issued.number)

    @write
    def _write_due_date_day(self):
        self._position = DUE_DATE_DAY_POSITION
        self._text = self._promissory_note_issued.due_date.strftime('%d')

    @write
    def _write_due_date_month(self):
        self._position = DUE_DATE_MONTH_POSITION
        self._text = self._promissory_note_issued.due_date.strftime('%B')

    @write
    def _write_due_date_year(self):
        self._position = DUE_DATE_YEAR_POSITION
        self._text = self._promissory_note_issued.due_date.strftime('%Y')

    @write
    def _write_long_due_date(self):
        self._position = LONG_DUE_DATE_POSITION
        self._text = self._promissory_note_issued.due_date.strftime('%d de %B de %Y')

    @write
    def _write_value(self):
        self._position = VALUE_POSITION
        self._text = f'{self._promissory_note_issued.value:.2f}'

    @write
    def _write_full_value(self):
        self._position = FULL_VALUE_POSITION
        self._text = f'R$ {self._promissory_note_issued.value:.2f}'

    @write
    def _write_beneficiary_name(self):
        self._position = BENEFICIARY_NAME_POSITION
        self._text = self._promissory_note_issued.beneficiary_name

    @write
    def _write_beneficiary_cpf(self):
        self._position = BENEFICIARY_NAME_CPF_POSITION
        self._text = self._promissory_note_issued.beneficiary_cpf

    @write
    def _write_city_and_state_payment(self):
        self._position = CITY_AND_STATE_PAYMENT_POSITION
        self._text = f'{self._promissory_note_issued.city_payment} - {self._promissory_note_issued.state_payment}'

    @write
    def _write_emitter_name(self):
        self._position = EMITTER_NAME_POSITION
        self._text = self._promissory_note_issued.emitter_name

    @write
    def _write_issuance_date_day(self):
        self._position = ISSUANCE_DATE_DAY_POSITION
        self._text = self._promissory_note_issued.issuance_date.strftime('%d')

    @write
    def _write_issuance_date_month(self):
        self._position = ISSUANCE_DATE_MONTH_POSITION
        self._text = self._promissory_note_issued.issuance_date.strftime('%m')

    @write
    def _write_issuance_date_year(self):
        self._position = ISSUANCE_DATE_YEAR_POSITION
        self._text = self._promissory_note_issued.issuance_date.strftime('%y')

    @write
    def _write_emitter_cpf(self):
        self._position = EMITTER_CPF_POSITION
        self._text = self._promissory_note_issued.emitter_cpf

    @write
    def _write_emitter_address(self):
        self._position = EMITTER_ADDRESS_POSITION
        self._text = self._promissory_note_issued.emitter_address

    def _create_filename(self):
        basename = f'{self._promissory_note_issued.number}_promissory_note.jpg'
        self._filename = path.join(CONTENT_DIR, basename)

    def _save_image(self):
        self._image.save(self._filename)

    def _write(self):
        self._draw.text(self._position, self._text, fill=TEXT_COLOR, font=TEXT_FONT)
