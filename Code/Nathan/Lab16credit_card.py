#Credit Card Validation




credit_input = list(input('Please enter your credit card number:\n'))
credit_input = list(map(int, credit_input))
credit_check = credit_input.pop()
print(credit_check)
#print(credit_check)


credit_input.reverse()


for x in range(0, len(credit_input), 2):
    credit_input[x] *= 2
    if credit_input[x] > 9:
        credit_input[x] -= 9
print(credit_input)
sum_credit_input = int(str(sum(credit_input))[1])
print(sum_credit_input)
#print(sum_credit_input)
if sum_credit_input == credit_check:
    print('Your credit card is valid')
else:
    print('Your credit card is not valid')




# # shorter example using list comprehensions
#
# cc = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'.split(' ')
# cc = [int(v) for v in cc]
# print(cc)
# cd = cc.pop()  # check digit
# print(cc, cd)
# cc = [cc[-i-1] for i in range(len(cc))]
# #cc = [(cc[i]*2 if cc[i]*2 <= 9 else cc[i]*2-9) if i%2 == 0 else cc[i] for i in range(len(cc))]
# cc = [cc[i]*2 if i%2 == 0 else cc[i] for i in range(len(cc))]
# cc = [v-9 if v > 9 else v for v in cc]
# print('valid' if int(str(sum(cc))[1]) == cd else 'invalid')
#
#
# # ex = [False if i%2 == 0 else True for i in range(10)]
# #
# # ex = []
# # for i in range(10):
# #     if i%2 == 0:
# #        ex.append(False)
# #     else:
# #         ex.append(True)





