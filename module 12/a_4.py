class Bank:
    def __init__(self):
        self.accounts = {}

    # ...

    def total_available_balance(self):
        return sum(account.balance for account in self.accounts.values())
