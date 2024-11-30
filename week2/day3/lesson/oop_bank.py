


class  BankAccount:
    ACCOUNT_AVAILABLE_NUMBER = 1000 #class attribute
    BANK_NAME = 'Hapoalim'

    def __init__(self, owner_name,balance = 0):
        self.__owner_name = owner_name #__private
        self.number = BankAccount.ACCOUNT_AVAILABLE_NUMBER
        self.transactions = []
        self._balance = balance #_protected
        BankAccount.ACCOUNT_AVAILABLE_NUMBER += 1

    @property #also called getter 
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value
        return self


    @classmethod #a method related to the class (not the object)
    def get_next_available_num(cls):
        return cls.ACCOUNT_AVAILABLE_NUMBER

    @staticmethod #a method that within the class but doesn't self(object)
    def conversion(amount, rate):
        return amount * rate

    def show_balance(self):
        print(f'Your balance now is {self._balance}')

    def deposit(self, amount, currency = 'shekels'):
        if currency == 'dollar':
            amount = self.conversion(amount, 3.77) # calling @staticmethod 
            self._balance += amount
        else:
            self._balance += amount          
            
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
    
    def __str__(self):
        output = f''' Account Number: {self.number} \nOwnerL {self._BankAccount__owner_name}\nBalance: {self.balance}'''
        return output
    
    def __iadd__(self, amount):
        self.deposit(amount)
        return self
    
    def __isub__(self, amount):
        self.withdraw(amount)
        return self
    
    def __lt__(self, other):
        if self.balance < other.balance:
            return True
        else: 
            return False


my_account = BankAccount('Juliana Schmidt', 156)
my_account2 = BankAccount('Daniel Schmidt', 100)

print(my_account < my_account2)
print(my_account2 < my_account)

# print(my_account)
# print(my_account.balance)

# my_account += 500
# my_account -= 200
# print(my_account.balance)


# do the conversion
# my_account.deposit(377, 'dollar')
# print(my_account.number)
# print(BankAccount.get_next_available_num())

# print(my_account.balance)
# my_account.balance = 50
# print(my_account.balance)


# my_account2 = BankAccount('Juliana Schmidt', 156)
# print(my_account2.number)
# my_account3 = BankAccount('Juliana Schmidt', 156)
# print(my_account3.number)

# print(BankAccount.BANK_NAME)

# my_account.deposit(500).withdraw(25).deposit(150).withdraw(25)

# print(my_account._balance)
# # # print(my_account.__owner_name) #give error
# print(my_account._BankAccount__owner_name)

#implement on those methods (except show_balance() a code that will add their action to the transactions list, and do a deposit and a withdraw and then print the transactions list to see the tracked information)