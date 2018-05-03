


import random

def random_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(0,99))
    return nums

def percent_sorted(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            count += 1
    return count / (len(nums)-1)

def swap_one(nums):
    r = nums.copy()
    i = random.randint(0, len(r)-1)
    j = random.randint(0, len(r)-1)
    r[i], r[j] = r[j], r[i]
    return r

list_length = 100
population_size = 100
percent_save = 0.1
n_save = int(population_size*percent_save)
population = []
for i in range(population_size):
    population.append(random_list(list_length))

while True:
    population.sort(key=lambda x: percent_sorted(x), reverse=True)
    top_ps = percent_sorted(population[0])
    print(top_ps)
    if top_ps == 1:
        print(population[0])
        break

    for i in range(n_save, len(population)):
        j = random.randint(0, n_save)
        population[i] = swap_one(population[j])



