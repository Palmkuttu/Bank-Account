# Bank Account OOP Project

## Description

This project implements a simple **Bank Account system using Object-Oriented Programming (OOP) in Python**.
The program models a bank account that can store transactions such as deposits and withdrawals and calculate the current balance.

## Features

* Create a bank account
* Deposit money
* Withdraw money
* Store transactions
* Calculate account balance
* Use special Python methods like `__str__` and `__repr__`

## Project Structure

```
bank_account_project/
│
├── account.py        # Account class
├── transaction.py    # Transaction class
├── test_account.py   # Tests for the account system
└── README.md         # Project documentation
```

## Account Class

The `Account` class represents a bank account.

### Properties

* `transactions` – A list that stores all transaction objects.

### Methods

* `deposit(amount)` – Adds a deposit transaction.
* `withdraw(amount)` – Adds a withdrawal transaction.
* `get_balance()` – Returns the current account balance.

## Example Usage

```python
from account import Account

account = Account()

account.deposit(100)
account.withdraw(30)

print(account.get_balance())
```

Output:

```
70
```

## Requirements

* Python 3.x

## How to Run

1. Clone the repository.
2. Open the project in your Python environment.
3. Run the Python files or tests.

## Author

Student: Dennis Zacharia
Course: Python Programming / OOP Assignment
