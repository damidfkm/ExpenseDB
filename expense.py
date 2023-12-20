import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, title, amount):
        expense = Expense(title, amount)
        self.expenses.append(expense)

    def remove_expense(self, id):
        self.expenses = [expense for expense in self.expenses if expense.id != id]

    def get_expense_by_id(self, id):
        for expense in self.expenses:
            if expense.id == id:
                return expense
        return None

    def get_expense_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]