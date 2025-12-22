class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print("Balance:", self.balance)


account1 = BankAccount("123456", "Harshith", 1000.0)
account1.deposit(500.0)
account1.display()
