class User:
    account_number = 1

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.number = User.account_number
        self.transactions = []
        self.loan_count = 0
        User.account_number += 1

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

    def transfer(self, target_user, amount):
        if amount > 0 and self.balance >= amount:
            target_user.balance += amount
            self.balance -= amount
            self.transactions.append(f"Transferred {amount} to Account Number {target_user.number}")
            target_user.transactions.append(f"Received {amount} from Account Number {self.number}")
            return f"Transferred {amount} to Account Number {target_user.number}. New balance: {self.balance}"
        if amount <= 0:
            return "Invalid transfer amount."
        if self.balance < amount:
            return "Insufficient funds for the transfer."

    def details(self):
        return f"Account Number: {self.number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: {self.balance}"

class Bank:
    def __init__(self):
        self.users = {}

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users[user.number] = user
        return user

    def get_user(self, account_number):
        return self.users.get(account_number)

def main():
    bank = Bank()

    while True:
        print("\nBanking Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = input("Account Type (Savings/Current): ").capitalize()
            if account_type in ["Savings", "Current"]:
                user = bank.create_account(name, email, address, account_type)
                print(f"Account created with Account Number: {user.number}")
            else:
                print("Invalid account type. Please choose Savings or Current.")

        elif choice == "2":
            account_number = int(input("Enter your Account Number: "))
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter the deposit amount: "))
                result = user.deposit(amount)
                print(result)
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "3":
            account_number = int(input("Enter your Account Number: "))
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter the withdrawal amount: "))
                result = user.withdraw(amount)
                print(result)
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "4":
            account_number = int(input("Enter your Account Number: "))
            user = bank.get_user(account_number)
            if user:
                print(user.check_balance())
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "5":
            account_number = int(input("Enter your Account Number: "))
            user = bank.get_user(account_number)
            if user:
                transactions = user.get_transaction_history()
                if transactions:
                    print("Transaction History:")
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transaction history.")
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "6":
            account_number = int(input("Enter your Account Number: "))
            user = bank.get_user(account_number)
            if user:
                amount = float(input("Enter the loan amount: "))
                result = user.take_loan(amount)
                print(result)
            else:
                print("Account not found. Please check the Account Number.")

        elif choice == "7":
            sender_account_number = int(input("Enter your Account Number: "))
            sender = bank.get_user(sender_account_number)
            if sender:
                receiver_account_number = int(input("Enter the receiver's Account Number: "))
                receiver = bank.get_user(receiver_account_number)
                if receiver:
                    amount = float(input("Enter the transfer amount: "))
                    result = sender.transfer(receiver, amount)
                    print(result)
                else:
                    print("Receiver's account not found. Please check the Account Number.")
            else:
                print("Sender's account not found. Please check the Account Number.")

        elif choice == "8":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")

if __name__ == "__main__":
    main()
