
tims_hangout_line = 'cool'



def is_even(a):
    return a% 2 == 0


def opposite(a, b):
    return (a < 0 and b > 0) or (b < 0 and a > 0)


def near_100(num):
    return num > 90 and num < 110
    # return abs(num-100) < 11


def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

    # b < a > c this works but angers Deraj
    # a > b > c this doesn't work


def print_powers_2():
    for i in range(21):
        print(2 ** i)


# part 2: strings --------------------------------------


def double_letters(text):
    output = ''
    for char in text:
        output += char * 2
    return output


def double_letters2(text):
    return ''.join(a * 2 for a in text)


# s = 'hello world'
# i = 3
# print(s[:i] + s[i+1:])

def missing_char(text):
    r = []
    for i in range(len(text)):
        r.append(text[:i] + text[i + 1:])
    return r


def latest_letter(text):
    letter_list = list(text)
    letter_list.sort()
    return letter_list[-1]
    # return sorted(list(text))[-1]


def latest_letter2(text):
    return chr(max(ord(c) for c in text))


def latest_letter3(text):
    max_value = -1
    for char in text:
        oc = ord(char)
        if oc > max_value:
            max_value = oc
    return chr(max_value)


import re


def count_hi(text):
    return len(re.findall(r'hi', text))


def count(to_find, text):
    return len(re.findall(to_find, text))


def count_cat_dog(text):
    text = text.lower()
    count_cat = count('cat', text)
    count_dog = count('dog', text)
    return count_cat == count_dog


def count_letter(letter, word):
    return count(letter, word)


count_letter = count
count_letter('i', 'antidisestablishmentterianism')


def lower_no_space(text):
    return text.lower().strip().replace('batman', 'BATMAN!')


# part 3: lists ---------------------------------------

def common_elements(nums1, nums2):
    return [n for n in nums1 if n in nums2]

    common_nums = []
    for n in nums1:
        if n in nums2
            common_nums.append(n)
    return common_nums


common_elements([5, 2, 3], [4, 5, 1])


def eveneven(nums):
    return len([n for n in nums if n % 2 == 0]) % 2 == 0

    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count % 2 == 0


eveneven([5, 6, 2])
eveneven([5, 5, 2])

mylist = []
while True:
    v = input('enter a value: ')
    try:
        mylist.append(int(v))
    except ValueError:
        break
print(mylist)


def reverse(nums):
    return reversed(nums)

    nums = nums.copy()
    nums.reverse()
    return nums

    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

        j = len(nums) - i - 1
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    nums2 = []
    for i in range(len(nums) - 1, -1, -1):
        nums2.append(nums[i])
    return nums2

    return [nums[i] for i in range(len(nums) - 1, -1, -1)]


def extract_less_than_ten(nums):
    return [n for n in nums if n < 10]


extract_less_than_ten([1, 2, 3, 11, 12, 13])  # [1, 2, 3]


def combine(nums1, nums2):
    if len(nums1) > len(nums2):  # ensure that nums2 is larger
        nums1, nums2 = nums2, nums1
    list1 = []
    for n in range(len(nums1)):
        list1.append(nums1[n])
        list1.append(nums2[n])
    list1.extend(nums2[len(nums1):])  # add the remaining elements from nums2 to list1
    return list1


combine(['a', 'b', 'c'], [1, 2, 3])  # → ['a', 1, 'b', 2, 'c', 3]


def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums))
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]


find_pair([5, 6, 2, 3], 7)  # [5, 2]

print(''.join(reversed('hello')))





# ----------------------------------------











def combine(nums1, nums2):
    if len(nums1) > len(nums2): # ensure that nums2 is larger
        nums1, nums2 = nums2, nums1
    list1 = []
    for n in range(len(nums1)):
        list1.append(nums1[n])
        list1.append(nums2[n])
    list1.extend(nums2[len(nums1):]) # add the remaining elements from nums2 to list1
    return list1



def combine2(nums1, nums2):
    #return [(nums1[i], nums2[i]) for i in range(len(nums1))]

    # for i in range(2*len(nums1)):
    #     0 -> 0
    #     1 -> 0
    #     2 -> 1
    #     3 -> 1

    return [nums1[i//2] if i % 2 == 0 else nums2[i//2] for i in range(2*len(nums1))]



#print(combine(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3]))  # → ['a', 1, 'b', 2, 'c', 3]
print(combine2(['a', 'b', 'c'], [1, 2, 3]))  # → ['a', 1, 'b', 2, 'c', 3]












def common_elements(nums1, nums2):
    return [n for n in nums1 if n in nums2]

print(common_elements([5, 2, 3, 1], [4, 5, 1]))













import re
def count_hi(text):
    return len(re.findall(r'hi', text))

print(count_hi('hihiyohhi'))




def latest_letter(text):
    # letter_list = list(text)
    # letter_list.sort()
    # return letter_list[-1]


    return sorted(list(text))[-1]

def latest_letter2(text):
    return chr(max(ord(c) for c in text))


def latest_letter3(text):
    max_value = -1
    for char in text:
        oc = ord(char)
        if oc > max_value:
            max_value = oc
    return chr(max_value)





print(latest_letter2('pneumonoultramicroscopicsilicovolcanoconiosis'))






def missing_char(text):
    r = []
    for i in range(len(text)):
        r.append(text[:i] + text[i+1:])
    return r


print(missing_char('hello world'))
























def a_is_largest(a, b, c):
    # return b < a > c
    return a > b > c

import random

print(a_is_largest(5, 2, 1))
print(a_is_largest(5, 2, 6))
print(a_is_largest(2, 2, 1))
print(a_is_largest(5, 1, 2))

total = 100000
count_same = 0

for i in range(total):

    a = random.randint(1,99)
    b = random.randint(1,99)
    c = random.randint(1,99)

    if (b < a > c) == (a > b and a > c):
        count_same += 1

print(f'{round(count_same/total*100,2)}%')













