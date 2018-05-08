cc_info = list(input("Give me your credit card info.. I promise it will be safe...\n:"))

check_digit = cc_info.pop()

print(f"{check_digit} check number")

cc_info = list(map(int, cc_info))

cc_info.reverse()


for x in range(0, len(cc_info), 2):
    cc_info[x] *= 2
    if cc_info[x] > 9:
        cc_info[x] -= 9

sum_cc_info = str(sum(cc_info))[-1]


print(f"{sum_cc_info} last digit")

if check_digit == sum_cc_info:
    print("Number Valid")
else:
    print("Number Not Valid")
