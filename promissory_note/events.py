from dataclasses import dataclass, field
from datetime import date


@dataclass
class PromissoryNoteIssued:
    number: int
    due_date: date
    value: float
    beneficiary_name: str
    beneficiary_cpf: str
    beneficiary_email: str
    currency: str
    city_payment: str
    state_payment: str
    emitter_name: str
    emitter_cpf: str
    emitter_address: str
    emitter_email: str
    issuance_date: date
    notifications: list = field(default_factory=list)


@dataclass
class PromissoryNoteNotIssued:
    notifications: list
