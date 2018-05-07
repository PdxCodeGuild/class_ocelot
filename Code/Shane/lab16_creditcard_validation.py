
cc_info = list(input("Give me your credit card info.. I promise it will be safe...\n:"))

check_digit = cc_info[-1]

cc_info = list(map(int,cc_info))

cc_info.remove(cc_info[-1])

cc_info.reverse()


for x in range(0,len(cc_info),2):
    cc_info[x] *= 2
    if cc_info[x] > 9:
        cc_info[x] -=9

sum_cc_info = str(sum(cc_info))

check_num = sum_cc_info[1]

if check_digit == check_num:
    print("Valid")
else:
    print("Not Valid")











