class Bank:
    def __init__(self):
        self.accounts = {}

    # ...

    def total_loan_amount(self):
        return sum(account.balance for account in self.accounts.values() if account.balance < 0)
