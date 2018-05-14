class Atm:
    def __init__(self):
        self.balance = 0
        self.interest = .0001
        self.transaction_list = []

    def check_balance(self): # returns the account balance
       return self.balance


    def deposit(self, amount): # deposits the given amount in the account
        self.balance += amount
        self.transaction_list.append(f'Deposited: \t${amount}')
        return f'New balance: $ {self.balance}'


    def check_withdrawal(self, amount): # returns true if the withdrawn amount won't put the account in the negative
        return self.balance >= amount

    def withdraw(self, amount): # withdraws the amount from the account and returns it
        self.balance -= amount
        self.transaction_list.append(f'Withdrew: \t${amount}')
        return f'New balance: $ {self.balance}'


    def calc_interest(self): # returns the amount of interest calculated on the account
        return self.balance * self.interest

    def transaction_rcpt(self):
        output = ''
        for transaction in self.transaction_list:
            output += transaction + '\n'
        return output




atm = Atm()                                                         # makes an instance of 'Class Atm'

# set values
atm.deposit(25000)                                                     # Deposit

# print results
print(f'Balance: {atm.check_balance()}')                            # Print balance.

withdraw_attempt = 700
print(f'${withdraw_attempt} withdrawal permitted? {atm.check_withdrawal(withdraw_attempt)}')         # Check withdrawal.

withdraw_amount = 25
atm.withdraw(withdraw_amount)                                                    # Withdraw.
print(f'Balance after ${withdraw_amount} withdrawal: $ {atm.check_balance()}')    # Print balance after withdrawal.

print(f'Interest on balance: ${atm.calc_interest()}')

print(f'\n\nTRANSACTIONS:\n{atm.transaction_rcpt()}')

