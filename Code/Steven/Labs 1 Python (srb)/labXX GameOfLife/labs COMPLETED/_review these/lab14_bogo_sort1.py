import random

# Make target string
def random_list(n):
    r = []

    for i in range(n):
        r.append(random.randint(0,10))

    # print(r, '\n')
    return r


def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0,len(nums)-1)
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t


def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogo_sort(nums):
    i = 0

    print(nums)
    while is_sorted(nums) != True:
        i += 1
        shuffle(nums)
        print(nums)



    print(f'That took {i} tries')

# Main
nums = random_list(10)

bogo_sort(nums)
print(nums)



# If no match, iterate.


# If match, indicate number of attempts and exit.


