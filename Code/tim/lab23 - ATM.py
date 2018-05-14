
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.trans = []

    def check_balance(self, tran=True):
        if tran:
            self.trans.append(['Check Balance', '-', '${:,.2f}'.format(self.balance)])
        return self.balance

    def deposit(self, amt):
        self.balance += amt
        self.trans.append(['Deposit', '${:,.2f}'.format(amt), '${:,.2f}'.format(self.balance)])

    def withdraw(self, amt):
        if self.check_withdraw(amt):
            self.balance -= amt
            self.trans.append(['Withdraw', '${:,.2f}'.format(amt), '${:,.2f}'.format(self.balance)])
            return True
        else:
            return False

    def check_withdraw(self, amt):
        return self.balance - amt >= 0

    def check_interest(self, time, r):
        return self.balance * time * r

    def transaction_receipt(self):
        return '\n'.join(['\t'.join(x) for x in self.trans])


def main():
    me = Customer('Tim Wilson', 1000000)
    while me.check_balance(False) > 0:
        a = input('''Welcome to the bank, what would you like to do?
OPTIONS: 1 = check bal, 2 = withdraw, 3 = deposit, 4 = trans log, 5 = calc interest
ENTRY > ''')
        if a == '1':
            print('Your balance is ' + '${:,.2f}'.format(me.check_balance()))
        elif a == '2':
            a = float(input('How Much?\n > '))
            r = me.withdraw(a)
            if r:
                print('Your new balance is ' + '${:,.2f}'.format(me.check_balance(False)))
            else:
                print('You tried to withdraw more than your current balance of ' + '${:,.2f}'.format(me.check_balance(False)))
        elif a == '3':
            a = float(input('How Much?\n > '))
            me.deposit(a)
            print('Your new balance is ' + '${:,.2f}'.format(me.check_balance(False)))
        elif a == '4':
            print(me.transaction_receipt())
        elif a == '5':
            t = float(input('How many years?\n > '))
            r = float(input('What rate?\n > '))
            print('You would earn ' + '${:,.2f}'.format(me.check_interest(t, r)))
        else:
            print('You failed to follow direction and forfeit ' + '${:,.2f}'.format(me.check_balance(False)))
            me.withdraw(me.check_balance())


main()


