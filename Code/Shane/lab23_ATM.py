import datetime
import collections



def now():
    date = datetime.datetime.now()
    return f'{date.year}-{date.month}-{date.day}, {date.hour}-{date.minute}-{date.second}'

class Atm:

    def __init__(self, name, id):
        self.balance = 0
        self.interest = .001
        self.name = name
        self.id = id
        self.transactions = collections.OrderedDict()
        self.transaction_count = 0
        self.date_opened = now()

    def __str__(self):
        return f'Account #: {self.id}\nOwner: {self.name}\nBalance: {self.balance}\nInterest: {self.check_interest()} Date Opened: {self.date_opened}\n\n'

    def checkbalance(self):
        self.transaction_count += 1
        self.transactions[self.transaction_count] = ('Check Balance', self.balance, now())
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1
        self.transactions[self.transaction_count] = ('Deposit', amount, now())
        return self.balance

    def check_withdrawal(self, amount):
        return self.balance >= amount

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transaction_count += 1
            self.transactions[self.transaction_count] = ('Withdrawal', amount, now())
            return self.balance
        else:
            self.transaction_count += 1
            self.transactions[self.transaction_count] = ('Withdrawal Failed', self.balance - amount)
            return f"Can't complete Transaction. Balance = {self.balance}"


    def check_interest(self):
        self.transaction_count += 1
        self.transactions[now()] = ('Check Interest', self.balance * self.interest)
        return f'${round(self.balance * self.interest, 2)}'



p1 = Atm('Shane', 70004672920)

p2 = Atm('Tim', 12489718394)

print(p1.balance, p2.balance)


p1.check_interest()

p1.deposit(2000)

print(p1)

p1.deposit(1000)

p2.deposit(9999)

print(p1)

p1.withdraw(500)

print(p1)

p1.withdraw(3001)

print(p1.transactions)

print(p1.balance, p2.balance)

