
def step_1_convert(in_str):
    return [int(c) for c in in_str]

def step_2_slice_check(in_lst):
    ck = in_lst.pop()
    return ck

def step_3_reverse(in_lst):
    in_lst.reverse()
    # out_lst = []
    # l = len(in_lst)
    # for i in range(l):
    #     out_lst.append(int(in_lst[l - len(out_lst) - 1]))
    # return out_lst

def step_4_double(rev_lst):
    for i in range(0, len(rev_lst), 2):
        rev_lst[i] *= 2

def step_5_sub9_over9(rev_lst):
    for i in range(len(rev_lst)):
        if rev_lst[i] > 9:
            rev_lst[i] -= 9

def step_6_sum_all(in_lst):
    t = 0
    for v in in_lst:
        t += v
    return t

def step_7_take_2nd(i):
    return int(str(i)[1])

def step_8_check_valid(sec, ck):
    return sec == ck


def main():
    in_str = input('Enter a credit card number\n > ')
    print(in_str)

    in_lst = step_1_convert(in_str)
    print(in_lst)

    ck = step_2_slice_check(in_lst)
    print(ck)

    step_3_reverse(in_lst)
    rev_lst = in_lst
    print(rev_lst)

    step_4_double(rev_lst)
    print(rev_lst)

    step_5_sub9_over9(rev_lst)
    print(rev_lst)

    sum_all = step_6_sum_all(rev_lst)
    print(sum_all)

    c2 = step_7_take_2nd(sum_all)
    print(c2)

    tf = step_8_check_valid(c2, ck)
    print(tf)

    if tf:
        print('Credit card is valid')
    else:
        print('Credit card is invalid')

main()
