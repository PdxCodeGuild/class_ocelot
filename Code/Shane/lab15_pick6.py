import random

how_many_numbers = 6

# pick_range has to be greater than or equal to how_many_numbers
# 1-?

pick_range = 100

times_to_run = 100000

balance = 0


def pick6(picks=how_many_numbers, pick_range=pick_range):
    pick6lst = []
    while len(pick6lst) != picks:
        rand_pick = random.randrange(1,pick_range)
        if rand_pick not in pick6lst:
            pick6lst.append(rand_pick)

    return pick6lst


def check_if_win(ticket, win_num, picks=how_many_numbers):
    win = {"0": 0, "1": 4, "2": 7, "3": 100, "4": 50000, "5": 1000000, "6": 25000000}
    count = 0
    for i in range(picks):
        if ticket[i] == win_num[i]:
            count += 1
    print()
    print(f"{count} numbers matched")
    winnings = win[str(count)]
    print(f"${winnings} winnings")

    return winnings


for i in range(times_to_run):
    winning_numbers = pick6()
    computer_ticket = pick6()
    print(f"{winning_numbers} winning numbers")
    print(f"{computer_ticket} computer ticket")
    balance -= 2
    addition = check_if_win(winning_numbers, computer_ticket)
    balance += addition

print(f"balance = {balance}")
print(f"ROI = {round((balance/(2*times_to_run))*100)}%")
