#try playing pick6 100,000 times, with the ticket cost and payoff below.
try_count = 0
cost_count = 0
import random
lotto_num_count = int(input('Enter quantity of numbers from 3 to 7 \n>'))
ticket_cost = int(input('Enter cost of ticket in whole dollars \n>'))
bank_acc = int(input('Enter the total amount willing to gamble'))
lottery_selections = []


num_winning = []
for i in range(lotto_num_count):
    num_winning.append(random.randint(1, 99))



num_try = []

while num_try != num_winning:
    num_try = []
    try_count += 1
    bank_acc -= ticket_cost
    if bank_acc <= 0:
        print('You lose make better life decisions')
        break
    for i in range(lotto_num_count):
        num_try.append(random.randint(1, 99))
    print(f'{num_winning} \t {num_try} \t {try_count} ${bank_acc} \n')
else:
    print('You Win')

