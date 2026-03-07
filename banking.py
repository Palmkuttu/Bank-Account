from datetime import datetime


class Transaction:
    def __init__(self, amount, timestamp=None):
        self.amount = float(amount)

        if timestamp is None:
            self.timestamp = datetime.now()
        else:
            self.timestamp = timestamp

    def __repr__(self):
       return f"Transaction(amount={self.amount}, {repr(self.timestamp)})"

    def __str__(self):
        sign = "+" if self.amount >= 0 else "-"
        amount = abs(self.amount)
        date = self.timestamp.date()
        return f"{date}: {sign}${amount:,.2f}"


class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        amount = abs(amount)
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def withdraw(self, amount):
        amount = -abs(amount)
        transaction = Transaction(amount)
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(t.amount for t in self.transactions)
