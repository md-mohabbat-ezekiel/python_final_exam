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

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_enabled = True  # Initialize the loan feature as enabled

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
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

    def list_all_accounts(self):
        return [account.details() for account in self.accounts.values()]

    def total_available_balance(self):
        return sum(account.balance for account in self.accounts.values())

    def total_loan_amount(self):
        return sum(account.balance for account in self.accounts.values() if account.balance < 0)

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled

    def is_loan_feature_enabled(self):
        return self.loan_feature_enabled

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def view_account_details(self, account_number):
        account = self.bank.get_account(account_number)
        if account:
            return account.details()
        return "Account not found. Please check the Account Number."

    def view_transaction_history(self, account_number):
        account = self.bank.get_account(account_number)
        if account:
            transactions = account.get_transaction_history()
            return transactions
        return "Account not found. Please check the Account Number."

def main():
    bank = Bank()
    admin = Admin(bank)

    while True:
        print("\nBanking Management System")
        print("1. Create Account")
        print("2. Admin: View Account Details")
        print("3. Admin: View Transaction History")
        print("4. Delete Account")
        print("5. List All Accounts")
        print("6. Check Total Balance")
        print("7. Check Total Loan Amount")
        print("8. Toggle Loan Feature")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            name, email, address, account_type = input("Name: "), input("Email: "), input("Address: "), input("Account Type (Savings/Current): ").capitalize()
            if account_type in ["Savings", "Current"]:
                account = bank.create_account(name, email, address, account_type)
                print(f"Account created with Account Number: {account.number}")
            else:
                print("Invalid account type. Please choose Savings or Current.")

        elif choice == "2":
            account_number = int(input("Enter the Account Number you want to view: "))
            print(admin.view_account_details(account_number))

        elif choice == "3":
            account_number = int(input("Enter the Account Number you want to view transaction history for: "))
            transactions = admin.view_transaction_history(account_number)
            if isinstance(transactions, list):
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            else:
                print(transactions)

        elif choice == "4":
            account_number = int(input("Enter the Account Number you want to delete: "))
            result = bank.delete_account(account_number)
            print(result)

        elif choice == "5":
            all_accounts = bank.list_all_accounts()
            if all_accounts:
                for account in all_accounts:
                    print(account)
            else:
                print("No accounts found.")

        elif choice == "6":
            total_balance = bank.total_available_balance()
            print(f"Total Available Balance in the Bank: {total_balance}")

        elif choice == "7":
            total_loan_amount = bank.total_loan_amount()
            print(f"Total Loan Amount in the Bank: {total_loan_amount}")

        elif choice == "8":
            bank.toggle_loan_feature()
            feature_status = "enabled" if bank.is_loan_feature_enabled() else "disabled"
            print(f"Loan Feature is now {feature_status}")

        elif choice == "9":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, or 9.")

if __name__ == "__main__":
    main()
