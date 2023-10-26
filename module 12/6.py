class Account:
    account_number = 1

    def __init__(self, name, email, address, account_type):
        self.name, self.email, self.address, self.account_type = name, email, address, account_type
        self.balance = 0
        self.number = Account.account_number
        self.transactions = []  # List to store transaction history
        self.loan_count = 0  # Initialize loan counter
        Account.account_number += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount} into {self.account_type} account")
            return f"Deposited {amount} into {self.account_type} account. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount} from {self.account_type} account")
            return f"Withdrew {amount} from {self.account_type} account. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds."

    def check_balance(self):
        return f"Available balance: {self.balance}"

    def get_transaction_history(self):
        return self.transactions

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transactions.append(f"Took a loan of {amount} from the bank")
            return f"Took a loan of {amount} from the bank. New balance: {self.balance}"
        return "You have already taken the maximum number of loans (2)."

    def details(self):
        return f"Account Number: {self.number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

# ... The rest of the code remains the same
