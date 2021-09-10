from marshmallow import post_load
from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Expense(Transaction):
    def __init__(self, description, amount):
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)
        # What makes it different is that it forces the "-abs(amount)" amount passed to be negative. Therefore, no matter if the user sends a positive or a negative value, we will store it as negative to facilitate calculations .
        
    def __repr__(self):
        return "<Expense(class={self.description!r})>".format(self=self)
    

class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self, data):
        return self.Expense(**data)