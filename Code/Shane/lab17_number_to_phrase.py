"""
I do not cover edge cases like 2twenty thousand,
it will say twoty thousand, but I do cover the lower numbers
like twenty nine etc.
"""


def z_to_19_dict(lst):
    if lst[0] == 1:
        return 10+lst[1]


z_19 = {   0: '',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten',
           11: 'eleven',
           12: 'twelve',
           13: 'thirteen',
           14: 'fourteen',
           15: 'fifteen',
           16: 'sixteen',
           17: 'seventeen',
           18: 'eighteen',
           19: 'nineteen',
           20: 'twenty',
           30: 'thirty',
           40: 'forty',
           50: 'fifty',
           60: 'sixty',
           70: 'seventy',
           80: 'eighty',
           90: 'ninety', }

x = 116989

remain = x

if x >= 100000:
    hundred_thousand = (remain // 100000)
    remain = x % 100000
    print(f'{z_19[hundred_thousand]} hundred', end =" ")
if x >= 10000:
    ten_thousand = (remain // 10000)
    remain = x % 10000
    print(f'{z_19[ten_thousand]}ty', end=" ")
if x >= 1000:
    thousand = (remain // 1000)
    remain = x % 1000
    print(f'{z_19[thousand]} thousand', end=" ")
if x >= 100:
    hundred = (remain // 100)
    remain = x % 100
    print(f'{z_19[hundred]} hundred and', end=" ")
if x >= 10:
    if remain < 20:
        lst = list(str(remain))
        lst = list(map(int,lst))
        print(f'{z_19[z_to_19_dict(lst)]}')
    else:
        lst = list(str(remain))
        lst = list(map(int,lst))
        print(f'{z_19[lst[0]*10]} {z_19[lst[-1]]}')
if x < 10:
    print(z_19[x])