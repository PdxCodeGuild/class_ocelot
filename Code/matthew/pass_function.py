

def apply_function(nums, f):
    for i in range(len(nums)):
        nums[i] = f(nums[i])

def double(x):
    return 2*x

nums = [1, 2, 3]
d = double
print(d(5))
apply_function(nums, d)
apply_function(nums, lambda x: 2*x)
print(nums)


k = lambda t: print(t)
k(5)
k('hello world!')

p = print
p('hello world!!')

def a():
    def b():
        print('this is bad')
    return b
a()()
