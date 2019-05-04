from datetime import datetime

from flask import Flask, render_template, request, redirect
from wtforms import Form, DateField, IntegerField, FloatField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from promissory_note.commands import IssuePromissoryNoteCommand
from promissory_note.gateways.services import PillowImageGenerationService, SendGridEmailPromissoryNoteIssued
from promissory_note.use_cases import IssuePromissoryNote

app = Flask(__name__)

validators = [DataRequired(message='Required')]


class IssuePromissoryNoteForm(Form):
    number = IntegerField(validators=validators, render_kw={'placeholder': 'Number'})
    due_date = DateField(validators=validators, format='%d/%m/%Y', render_kw={'placeholder': 'Due date'})
    value = FloatField(validators=validators, render_kw={'placeholder': 'Value'})
    beneficiary_name = StringField(validators=validators, render_kw={'placeholder': 'Beneficiary name'})
    beneficiary_cpf = StringField(validators=validators, render_kw={'placeholder': 'Beneficiary cpf'})
    beneficiary_email = StringField(validators=validators, render_kw={'placeholder': 'Beneficiary email'})
    currency = StringField(validators=validators, render_kw={'placeholder': 'Currency'})
    city_payment = StringField(validators=validators, render_kw={'placeholder': 'City payment'})
    state_payment = StringField(validators=validators, render_kw={'placeholder': 'State payment'})
    emitter_name = StringField(validators=validators, render_kw={'placeholder': 'Emitter name'})
    emitter_cpf = StringField(validators=validators, render_kw={'placeholder': 'Emitter cpf'})
    emitter_address = StringField(validators=validators, render_kw={'placeholder': 'Emitter address'})
    emitter_email = EmailField(validators=validators, render_kw={'placeholder': 'Emitter email'})
    issuance_date = DateField(validators=validators, format='%d/%m/%Y', render_kw={'placeholder': 'Issuance date'})

    @property
    def data(self):
        self._data = super().data

        self._parse_number()
        self._parse_due_date()
        self._parse_value()
        self._parse_issuance_date()

        del self._data['issuance_date']

        return dict(number=self._number,
                    due_date=self._due_date,
                    value=self._value,
                    issuance_date=self._issuance_date,
                    **self._data)

    def _parse_issuance_date(self):
        self._issuance_date = datetime.strptime(self.issuance_date.data, self.issuance_date.format).date()

    def _parse_value(self):
        self._value = float(self.number.data)
        del self._data['value']

    def _parse_due_date(self):
        self._due_date = datetime.strptime(self.due_date.data, self.due_date.format).date()
        del self._data['due_date']

    def _parse_number(self):
        self._number = int(self.number.data)
        del self._data['number']


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', issue_promissory_note_form=IssuePromissoryNoteForm())

    if request.method == 'POST':
        issue_promissory_note_form = IssuePromissoryNoteForm(data=request.form)

        if issue_promissory_note_form.validate():
            issue_promissory_note_command = IssuePromissoryNoteCommand(**issue_promissory_note_form.data)

            image_generation_service = PillowImageGenerationService()

            email_promissory_note_issued = SendGridEmailPromissoryNoteIssued()

            issue_promissory_note = IssuePromissoryNote(image_generation_service, email_promissory_note_issued)

            issue_promissory_note.execute(issue_promissory_note_command)

            return redirect('/')

        return render_template('index.html', issue_promissory_note_form=issue_promissory_note_form)
