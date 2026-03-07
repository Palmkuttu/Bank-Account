import datetime as dt
from banking import Transaction, Account


def test_transaction_amount():
    t = Transaction(100)
    assert t.amount == 100


def test_transaction_timestamp_default():
    t = Transaction(100)
    assert isinstance(t.timestamp, dt.datetime)


def test_transaction_timestamp_custom():
    time = dt.datetime(2002, 1, 10)
    t = Transaction(50, time)
    assert t.timestamp == time


def test_transaction_repr():
    time = dt.datetime(2002, 1, 10)
    t = Transaction(10, time)
    assert repr(t) == f"Transaction(amount=10.0, timestamp={repr(time)})"


def test_account_deposit():
    acc = Account()
    acc.deposit(100)
    assert acc.transactions[0].amount == 100


def test_account_withdraw():
    acc = Account()
    acc.withdraw(50)
    assert acc.transactions[0].amount == -50


def test_balance():
    acc = Account()
    acc.deposit(100)
    acc.withdraw(90)
    acc.deposit(10)
    assert acc.get_balance() == 20
