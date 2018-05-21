class Atm:
    def __init__(self):
        self.balance = 0
        self.interest = .001
        self.account_ledger = []
     # attributes:
     #check_balance()returns the account balance
    def check_balance(self):
        return self.balance

    #deposit(amount)deposits the given amount in the account
    def deposit_amount(self, amount):
        self.balance += amount
        self.account_ledger.append(f'Deposited ${amount}')
        return f'New balance: ${self.balance}'
    #check_withdrawl(amount)returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawl(self, amount):
        return self.balance >= amount


    #withdraw(amount) withdraws the amount from the account and returns it
    def withdraw_amount(self, amount):
        self.balance -= amount
        self.account_ledger.append(f'Withdrew ${amount}')
        return f'New balance: ${self.balance}'


    #calc_interest()returns the amount of interest calculated on the account
    def calc_interest(self):
        return self.balance *self.interest

    def ledger(self):
        output = ''
        for transaction in self.account_ledger:
            output += transaction + '\n'
        return output

# Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

atm = Atm()

atm.deposit_amount(11150)

check_balance = atm.check_balance()
#print(atm.check_withdrawl(100))
#print(atm.withdraw_amount(50))
#print(atm.calc_interest())
print(atm.deposit_amount(50))
print(atm.withdraw_amount(150))

print(atm.ledger())

