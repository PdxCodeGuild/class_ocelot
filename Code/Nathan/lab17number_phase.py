num_list = int(input('Please enter a number 0-999:\n'))
ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds_list = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']
num_list_10 = num_list // 10
print(num_list_10)
num_list_1 = num_list % 10
num_list_100 = num_list // 100
print(num_list_100)
if num_list_10 == 1:
    print(teens_list[num_list_1 -1])
#if num_list_100 >= 1:
    #print(f'{ hundreds_list[num_list_100 -1]}-{ tens_list[num_list_10 -1]}-{ones_list[num_list_1]}')
elif num_list_10 == 0:
    print(ones_list[num_list_1])
else:
    print(f'{tens_list[num_list_10 -1]}-{ones_list[num_list_1]}')




