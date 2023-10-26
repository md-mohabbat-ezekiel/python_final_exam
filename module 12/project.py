class Account:
    account_number = 1

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.number = Account.account_number
        self.transactions = []
        self.loan_count = 0
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
        return "Withdrawal amount exceeded" if amount > self.balance else "Invalid withdrawal amount."

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

    def transfer(self, target_account, amount):
        if amount > 0 and self.balance >= amount:
            target_account.balance += amount
            self.balance -= amount
            self.transactions.append(f"Transferred {amount} to Account Number {target_account.number}")
            target_account.transactions.append(f"Received {amount} from Account Number {self.number}")
            return f"Transferred {amount} to Account Number {target_account.number}. New balance: {self.balance}"
        if amount <= 0:
            return "Invalid transfer amount."
        if self.balance < amount:
            return "Insufficient funds for the transfer."

    def details(self):
        return f"Account Number: {self.number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

class User:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts[account.number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

class Admin(User):
    def delete_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            del self.accounts[account_number]
            return "Account deleted successfully."
        return "Account not found. Please check the Account Number."

class Bank:
    def __init__(self):
        self.users = {"user": User(), "admin": Admin()}

def main():
    bank = Bank()

    while True:
        print("\nBanking Management System")
        print("1. User: Create Account")
        print("2. User: Deposit")
        print("3. User: Withdraw")
        print("4. User: Check Balance")
        print("5. User: Transaction History")
        print("6. User: Take Loan")
        print("7. User: Transfer Money")
        print("8. Admin: Delete Account")
        print("9. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == "1":
            user_type = input("User Type (user/admin): ").lower()
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Account Type (Savings/Current): ").capitalize()
            if user_type in bank.users:
                user = bank.users[user_type].create_account(name, email, address, account_type)
                print(f"Account created with Account Number: {user.number}")
            else:
                print("Invalid user type. Please choose 'user' or 'admin'.")

        elif choice in ["2", "3", "4", "5", "6", "7"]:
            user_type = input("User Type (user/admin): ").lower()
            account_number = int(input("Enter your Account Number: "))
            if user_type in bank.users and account_number in bank.users[user_type].accounts:
                user = bank.users[user_type].get_account(account_number)
                if choice == "2":
                    amount = float(input("Enter the deposit amount: "))
                    result = user.deposit(amount)
                    print(result)
                elif choice == "3":
                    amount = float(input("Enter the withdrawal amount: "))
                    result = user.withdraw(amount)
                    print(result)
                elif choice == "4":
                    print(user.check_balance())
                elif choice == "5":
                    transactions = user.get_transaction_history()
                    if transactions:
                        print("Transaction History:")
                        for transaction in transactions:
                            print(transaction)
                    else:
                        print("No transaction history.")
                elif choice == "6":
                    amount = float(input("Enter the loan amount: "))
                    result = user.take_loan(amount)
                    print(result)
                elif choice == "7":
                    target_account_number = int(input("Enter the receiver's Account Number: "))
                    target_account = bank.users[user_type].get_account(target_account_number)
                    amount = float(input("Enter the transfer amount: "))
                    result = user.transfer(target_account, amount)
                    print(result)
            else:
                print("Account not found. Please check the User Type and Account Number.")

        elif choice == "8":
            if "admin" in bank.users:
                admin = bank.users["admin"]
                account_number = int(input("Enter the Account Number you want to delete: "))
                result = admin.delete_account(account_number)
                print(result)
            else:
                print("Admin user not found. Please create an admin account first.")

        elif choice == "9":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8, or 9.")

if __name__ == "__main__":
    main()
