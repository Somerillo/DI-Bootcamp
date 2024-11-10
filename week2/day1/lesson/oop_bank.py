class BankAccount:
    def __init__(self, owner_name, number, balance=0):
        self.owner_name = owner_name
        self.number = number
        self.transactions = []
        self.balance = balance

    def show_balance(self):
        print(f"el balance es {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.transactions.append(f"deposit {amount}")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self.show_balance()
        self.transactions.append(f"retiro {amount}")
        return self.balance

    def show_transactions(self):
        for i, track in enumerate(self.transactions):
            print(f"transaccion {i+1}: {track}")
        return self.show_balance()


my_account = BankAccount("nombre usuario", 928349, 100.00)
my_account.deposit(1.59)
my_account.withdraw(398.59)
print(my_account.balance)

# inplement on those methods, except show_balance(),  a code that will add their action to the transactions list

print(my_account.transactions)


my_account.deposit(1.59)
my_account.withdraw(398.59)
my_account.deposit(54)
my_account.withdraw(4564)
my_account.deposit(34643)
my_account.withdraw(14359)
my_account.show_transactions()
# my_account