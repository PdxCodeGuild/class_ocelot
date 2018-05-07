num_list = int(input('Please enter a number 0-99:\n'))
ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num_list_10 = num_list // 10
num_list_1 = num_list % 10

if num_list_10 == 1:
   print(teens_list[num_list_1 -1])

elif num_list_10 == 0:
    print(ones_list[num_list_1])
else:
    print(f'{tens_list[num_list_10 -1]}-{ones_list[num_list_1]}')




