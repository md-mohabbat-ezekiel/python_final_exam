class Account:
    account_number = 1

    def __init__(self, name, email, address, account_type):
        self.name, self.email, self.address, self.account_type = name, email, address, account_type
        self.balance = 0
        self.number = Account.account_number
        self.transactions = []  # List to store transaction history
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

    def details(self):
        return f"Account Number: {self.number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts[account.number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

def main():
    bank = Bank()

    while True:
        print("\nBanking Management System")
        print("1. Create Account")
        print("2. View Account Details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            name, email, address, account_type = input("Name: "), input("Email: "), input("Address: "), input("Account Type (Savings/Current): ").capitalize()
            if account_type in ["Savings", "Current"]:
                account = bank.create_account(name, email, address, account_type)
                print(f"Account created with Account Number: {account.number}")
            else:
                print("Invalid account type. Please choose Savings or Current.")

        elif choice == "2":
            account_number = int(input("Enter your Account Number: "))
            account = bank.get_account(account_number)
            if account:
                print(account.details())
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "3":
            account_number, amount = int(input("Enter your Account Number: ")), float(input("Enter the deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                print(account.deposit(amount))
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "4":
            account_number, amount = int(input("Enter your Account Number: ")), float(input("Enter the withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                if amount > account.balance:
                    print("Withdrawal amount exceeded.")
                else:
                    print(account.withdraw(amount))
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "5":
            account_number = int(input("Enter your Account Number: "))
            account = bank.get_account(account_number)
            if account:
                print(account.check_balance())
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "6":
            account_number = int(input("Enter your Account Number: "))
            account = bank.get_account(account_number)
            if account:
                transactions = account.get_transaction_history()
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "7":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

if __name__ == "__main__":
    main()
