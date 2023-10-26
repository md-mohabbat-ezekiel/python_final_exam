class Admin:
    def __init__(self, bank):
        self.bank = bank

    # ...

    def list_all_accounts(self):
        return [account.details() for account in self.bank.accounts.values()]
