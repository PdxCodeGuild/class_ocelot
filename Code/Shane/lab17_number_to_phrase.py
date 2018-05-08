
def z_to_19_dict(lst):
    the_num = 0
    if lst[1] == 1:
        for i in range(10):
            if i == lst[0]:
                the_num = int("1" + str(i))
                return the_num
    else:
        return lst[0]



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
           19: 'nineteen',}
twenty_ = {
           2: 'twenty',
           3: 'thirty',
           4: 'forty',
           5: 'fifty',
           6: 'sixty',
           7: 'seventy',
           8: 'eighty',
           9: 'ninety',}
hundreds= {
           1: 'hundred',}
thousand= {
           1: 'thousand'
           }




x = "57"

num_lst = list(x)
num_lst.reverse()
int_lst = list(map(int,num_lst))

one_t0_19 = z_to_19_dict(int_lst)

print(z_19[one_t0_19])

output = []
if len(int_lst) == 3:
    output.append(z_19[int_lst[2]])
    output.append(hundreds[1])
if :
    output.append(z_19[z_to_19_dict(int_lst)])

print(output)
#
# ones = (num_lst[1]+num_lst[0])
#
# print(ones)
#
# ones = int(ones)
#
# print(type(ones))
#
# print()
#
# x_int = int(x)
#
# for i in range(len(num_lst)):
#     tens = ""
#     hundreds = ""
#     print(i)
#     print()
#     if i == 1 or num_lst[1] == 1:
#         print(ten_19[i-1])
#
# for x in range(len(x)):
#     if x == 0:
#         break_lst.append(x_int % 10)
#         print(break_lst)
#     if x == 1:
#         break_lst.append(x_int % 100// 10)
#         print(break_lst)
#     if x == 2:
#         break_lst.append(x_int % 1000 //100)
#         print(break_lst)
#     if x == 3:
#         break_lst.append(x_int % 10000)
#         print(break_lst)