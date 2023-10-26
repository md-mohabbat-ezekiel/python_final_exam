class Account:
    account_number = 1

    def __init__(self, name, email, address, account_type):
        self.name, self.email, self.address, self.account_type = name, email, address, account_type
        self.balance = 0
        self.number = Account.account_number
        Account.account_number += 1

    def details(self):
        return f"Account Number: {self.number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

# Creating an account
account1 = Account("John Doe", "johndoe@example.com", "123 Main Street", "Savings")

# Accessing account details
print(account1.details())
