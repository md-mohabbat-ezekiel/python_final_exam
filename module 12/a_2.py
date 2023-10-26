class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, email, address, account_type):
        account = account(name, email, address, account_type)
        self.accounts[account.number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def delete_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            del self.accounts[account_number]
            return "Account deleted successfully."
        return "Account not found. Please check the Account Number."
