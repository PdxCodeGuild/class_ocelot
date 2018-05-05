import random

# set variables
lotto_num_count = 2                             # lotto info
lotto_payout = 10000
lotto_tkt_cost = 3

your_bank_account = 10000                       # your info

lotto_tkts_purchased = 0                        # your behavior
lotto_tkt_cost_tot = 0

# set text messages
msg_welcome = f'\nWELCOME TO LOTTO SIMULATOR PRO VI SUITE TRIAL HOME EDITION®\n'
msg_end_win = 'You \"Win\"!'
msg_end_lose = 'You Lose!'

print(msg_welcome)


num_win = []                                    # define the 'winning numbers' list
for i in range(lotto_num_count):                # for n times...
    num_win.append(random.randint(1, 99))       # pick a number from 1 to 99

# Buy lottery tickets.
num_try = []                                    # make list for the lotto number picker

while num_try != num_win:                       # while the nums do NOT match...
    num_try = []                                # zero out the lotto number picker before new pick
    lotto_tkts_purchased += 1                   # increment num of lotto tkts purchased
    your_bank_account -= lotto_tkt_cost         # decrement your bank acct by ticket cost
    for i in range(lotto_num_count):            # the numbers on the newly purchased ticked
        num_try.append(random.randint(1, 99))   # pick a number from 1 to 99

    # ticket purchase tracker
    number_compare = f'Winning nums: {num_win}\tYour nums:{num_try}\t'
    if your_bank_account - lotto_tkt_cost <= 0: # you're out of money
        print(f'\n{msg_end_lose}')
        cost_total = lotto_tkt_cost * lotto_tkts_purchased
        r_o_i = round((((cost_total * -1)) / lotto_payout) * 100)
        print(f'\nYOU SPENT:\t\t${cost_total} on {lotto_tkts_purchased} tickets')
        print(f'RETURN ON INVESTMENT:\t{r_o_i}%\n')
        print(f'BANK ACCOUNT BALANCE:\t${your_bank_account}')
        break

    print(f'{number_compare}\tTry # {lotto_tkts_purchased}\tAcct: ${your_bank_account}')

else:                                           # You "Win"
    cost_total = lotto_tkt_cost * lotto_tkts_purchased


    r_o_i = round((((cost_total * -1))/lotto_payout)*100)

    print(f'\nYOU SPENT:\t\t${cost_total} on {lotto_tkts_purchased} tickets')
    print(f'YOU WON:\t\t${lotto_payout}')

    print(f'ROI:\t {r_o_i}%\n')

    print(f'BANK ACCOUNT BALANCE:\t${your_bank_account + lotto_payout}')

    print(f'\n{msg_end_win}')





