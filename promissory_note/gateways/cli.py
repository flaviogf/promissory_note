from datetime import datetime

import click

from promissory_note.commands import IssuePromissoryNoteCommand
from promissory_note.gateways.services import PillowImageGenerationService
from promissory_note.use_cases import IssuePromissoryNote


@click.command()
@click.option('--number', prompt=True, type=int)
@click.option('--due-date', prompt=True, type=str)
@click.option('--value', prompt=True, type=float)
@click.option('--beneficiary-name', prompt=True, type=str)
@click.option('--beneficiary-cpf', prompt=True, type=str)
@click.option('--beneficiary-email', prompt=True, type=str)
@click.option('--currency', prompt=True, type=str)
@click.option('--city-payment', prompt=True, type=str)
@click.option('--state-payment', prompt=True, type=str)
@click.option('--emitter-name', prompt=True, type=str)
@click.option('--emitter-cpf', prompt=True, type=str)
@click.option('--emitter-address', prompt=True, type=str)
@click.option('--emitter-email', prompt=True, type=str)
@click.option('--issuance-date', prompt=True, type=str)
def main(number,
         due_date,
         value,
         beneficiary_name,
         beneficiary_cpf,
         beneficiary_email,
         currency,
         city_payment,
         state_payment,
         emitter_name,
         emitter_cpf,
         emitter_address,
         emitter_email,
         issuance_date):
    promissory_note(number,
                    due_date,
                    value,
                    beneficiary_name,
                    beneficiary_cpf,
                    beneficiary_email,
                    currency,
                    city_payment,
                    state_payment,
                    emitter_name,
                    emitter_cpf,
                    emitter_address,
                    emitter_email,
                    issuance_date)


def promissory_note(number,
                    due_date,
                    value,
                    beneficiary_name,
                    beneficiary_cpf,
                    beneficiary_email,
                    currency,
                    city_payment,
                    state_payment,
                    emitter_name,
                    emitter_cpf,
                    emitter_address,
                    emitter_email,
                    issuance_date):
    image_generation_service = PillowImageGenerationService()

    email_service = lambda x: print(f'Send email {x}...')

    issue_promissory_note = IssuePromissoryNote(image_generation_service=image_generation_service,
                                                email_service=email_service)

    issue_promissory_note_command = IssuePromissoryNoteCommand(number=number,
                                                               due_date=datetime.strptime(due_date, '%d/%m/%Y').date(),
                                                               value=value,
                                                               beneficiary_name=beneficiary_name,
                                                               beneficiary_cpf=beneficiary_cpf,
                                                               beneficiary_email=beneficiary_email,
                                                               currency=currency,
                                                               city_payment=city_payment,
                                                               state_payment=state_payment,
                                                               emitter_name=emitter_name,
                                                               emitter_cpf=emitter_cpf,
                                                               emitter_address=emitter_address,
                                                               emitter_email=emitter_email,
                                                               issuance_date=datetime.strptime(issuance_date,
                                                                                               '%d/%m/%Y').date())

    issue_promissory_note.execute(command=issue_promissory_note_command)

    print('Emission request sent')


if __name__ == '__main__':
    main()
