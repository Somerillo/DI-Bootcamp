class  BankAccount:
    def __init__(self, owner_name,number,balance = 0):
        self.__owner_name = owner_name #__private
        self.number = number
        self.transactions = []
        self._balance = balance #_protected

    def show_balance(self):
        print(f'Your balance now is {self.balance}')

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.transactions.append(f'Deposit: {amount}')
        return self      
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self.transactions.append(f'Withdraw: {- amount}')
        else:
            print('You don`t have enough balance')
            self.show_balance()
        return self
    
    def show_transactions(self):
        for i, track in enumerate(self.transactions):
            print(f'transaction {i+1}: {track}')
        return self.show_balance()


my_account = BankAccount('Juliana Schmidt', 156, 100)
my_account.deposit(500).withdraw(25).deposit(150).withdraw(25)

print(my_account._balance)
# # print(my_account.__owner_name) #give error
print(my_account._BankAccount__owner_name)






#implement on those methods (except show_balance() a code that will add their action to the transactions list, and do a deposit and a withdraw and then print the transactions list to see the tracked information)