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
