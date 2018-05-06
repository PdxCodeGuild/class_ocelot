

def single_digit(num_str):
    if num_str == '0':
        return 'Zero'
    elif num_str == '1':
        return 'One'
    elif num_str == '2':
        return 'Two'
    elif num_str == '3':
        return 'Three'
    elif num_str == '4':
        return 'Four'
    elif num_str == '5':
        return 'Five'
    elif num_str == '6':
        return 'Six'
    elif num_str == '7':
        return 'Seven'
    elif num_str == '8':
        return 'Eight'
    else:
        return 'Nine'


def teens(num_str):
    if num_str == '0':
        return 'Ten'
    elif num_str == '1':
        return 'Eleven'
    elif num_str == '2':
        return 'Twelve'
    elif num_str == '3':
        return 'Thirteen'
    elif num_str == '5':
        return 'Fifteen'
    else:
        return single_digit(num_str) + 'teen'


def tens(num_str):
    if num_str == '2':
        return 'Twenty'
    elif num_str == '3':
        return 'Thirty'
    elif num_str == '4':
        return 'Forty'
    elif num_str == '5':
        return 'Fifty'
    elif num_str == '6':
        return 'Sixty'
    elif num_str == '7':
        return 'Seventy'
    elif num_str == '8':
        return 'Eighty'
    else:
        return 'Ninety'




num_str = input('What number do you want to translate into words?\n > ')
num_list = list(num_str)

if len(num_list) == 1:
    print(single_digit(num_str))
elif len(num_list) == 2:
    if num_list[0] == '1':
        print(teens(num_list[1]))
    else:
        pre = tens(num_list[0])
        suf = single_digit(num_list[1])
        print(pre + '-' + suf.lower())
else:
    h = single_digit(num_list[0]) + ' hundred '
    if num_list[1] == '1':
        t = teens(num_list[2]).lower() + ' '
    elif int(num_list[1]) > 1:
        t = tens(num_list[1]).lower() + ' '
    else:
        t = ''
    if int(num_list[2]) > 0:
        s = single_digit(num_list[2]).lower()
    else:
        s = ''
    print(h + t + s)
