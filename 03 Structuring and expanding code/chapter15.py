# chapter15.py
# OOP: classes, dataclasses, properties
from dataclasses import dataclass, field
from datetime import date

@dataclass(slots=True)
class Task:
    id: int
    title: str
    done: bool = False
    due: date | None = None
    tags: list[str] = field(default_factory=list)

    def mark_done(self) -> None:
        self.done = True

    @property
    def is_overdue(self) -> bool:
        return (self.due is not None) and (date.today() > self.due)

# Traditional class when you need control
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount
