from promissory_note.entities import Beneficiary, Emitter, PromissoryNote
from promissory_note.value_objects import Name, Cpf, Email


class IssuePromissoryNote:
    def __init__(self, image_generation_service, email_promissory_note_issued):
        self._image_generation_service = image_generation_service
        self._email_promissory_note_issued = email_promissory_note_issued

    def execute(self, command):
        beneficiary = Beneficiary(name=Name(command.beneficiary_name),
                                  cpf=Cpf(command.beneficiary_cpf),
                                  email=Email(command.beneficiary_email))

        emitter = Emitter(name=Name(command.emitter_name),
                          cpf=Cpf(command.emitter_cpf),
                          address=command.emitter_address,
                          email=Email(command.emitter_email))

        promissory_note = PromissoryNote(number=command.number,
                                         due_date=command.due_date,
                                         value=command.value,
                                         currency=command.currency,
                                         city_payment=command.city_payment,
                                         state_payment=command.state_payment,
                                         issuance_date=command.issuance_date,
                                         beneficiary=beneficiary,
                                         emitter=emitter)

        promissory_note.attach(self._image_generation_service, self._email_promissory_note_issued)

        promissory_note.issue()
